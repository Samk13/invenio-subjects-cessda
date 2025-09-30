#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from collections.abc import Iterable, Sequence
from datetime import datetime, timezone
from pathlib import Path

from click import secho
from yaml import safe_dump

from invenio_subjects_cessda.delta import (
    build_delta_report,
    load_previous_snapshot,
    write_delta_report,
)
from invenio_subjects_cessda.schemas import cessda_schema
from invenio_subjects_cessda.utils import logger

VOCAB_FIELDS = ("id", "scheme", "subject")
TIMESTAMP_FORMAT = "%Y%m%dT%H_%M%S"


def _sort_key(entry: dict) -> tuple[str, str]:
    subject = (entry.get("subject") or "").strip().lower()
    identifier = entry.get("id") or ""
    return subject, identifier


def _normalise_entries(data: Sequence[dict]) -> list[dict]:
    """Flatten and normalise raw vocabulary payloads."""
    entries: list[dict] = []
    for vocabulary in data:
        vocabulary_name = vocabulary.get("name", "")
        for raw_entry in vocabulary.get("data", []):
            normalised = cessda_schema(raw_entry)
            if not normalised:
                continue
            normalised["vocabulary"] = vocabulary_name
            entries.append(normalised)

    entries.sort(key=_sort_key)
    logger.debug("Normalised %s vocabulary entries", len(entries))
    return entries


def _prune_for_yaml(entries: Iterable[dict]) -> list[dict]:
    """Project entries to the public YAML representation."""
    return [{field: entry[field] for field in VOCAB_FIELDS} for entry in entries]


def _build_dated_delta_path(base_path: Path, timestamp: datetime) -> Path:
    """Return a timestamped filename for the delta report."""

    suffix = base_path.suffix
    stem = base_path.stem
    formatted = timestamp.strftime(TIMESTAMP_FORMAT)
    filename = f"{stem}_{formatted}{suffix}"
    return base_path.with_name(filename)


def _merge_with_previous_snapshot(
    current_entries: Sequence[dict], previous_entries: Sequence[dict]
) -> list[dict]:
    """Keep prior vocab entries and append genuinely new ones."""

    if not previous_entries:
        # First run - nothing to preserve, return current snapshot verbatim.
        return list(current_entries)

    merged: list[dict] = [dict(entry) for entry in previous_entries]

    seen_ids = {entry["id"] for entry in previous_entries if entry.get("id")}

    for entry in current_entries:
        vocab_id = entry.get("id")
        if vocab_id and vocab_id in seen_ids:
            continue

        merged.append(entry)
        if vocab_id:
            seen_ids.add(vocab_id)

    merged.sort(key=_sort_key)
    return merged


def _write_yaml(entries: Sequence[dict], destination: Path) -> None:
    """Persist YAML vocabulary payload to disk."""
    logger.debug("Writing %s entries to '%s'", len(entries), destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as yaml_f:
        safe_dump(entries, yaml_f, sort_keys=False, allow_unicode=True)


def _reuse_existing_ids(
    entries: list[dict], previous_entries: Sequence[dict]
) -> list[dict]:
    """Reuse identifiers for matching subjects to avoid duplicates in updates."""

    if not previous_entries:
        return entries

    previous_by_subject = {
        item["subject"].strip().lower(): item
        for item in previous_entries
        if item.get("subject") and item.get("id")
    }

    merged: list[dict] = []
    seen_subjects: set[str] = set()

    for entry in entries:
        subject = entry["subject"].strip()
        subject_key = subject.lower()

        if subject_key in seen_subjects:
            continue

        previous = previous_by_subject.get(subject_key)
        if previous:
            entry["id"] = previous["id"]
            if previous.get("scheme"):
                entry["scheme"] = previous["scheme"]

        merged.append(entry)
        seen_subjects.add(subject_key)

    return merged


def convert_vocabularies(
    data: Sequence[dict],
    output_path: str,
    delta_path: str | None = None,
    retain_removed_entries: bool = True,
) -> None:
    """Convert fetched vocabularies to YAML and record a delta report.

    Parameters
    ----------
    data:
        Raw vocabulary payloads grouped by vocabulary name.
    output_path:
        Destination for the consolidated YAML export.
    delta_path:
        Base path for the JSON delta report (timestamp will be appended).
    retain_removed_entries:
        When ``True`` (default) previously exported entries missing from the
        current payload remain in the YAML so they can be reintroduced later.
        When ``False`` the output only contains entries present in the latest
        fetch, effectively pruning removed vocabularies.
    """

    logger.debug("Convert vocabularies started ...")
    destination = Path(output_path)
    delta_destination = Path(delta_path) if delta_path else None
    timestamp = datetime.now(timezone.utc)

    current_entries = _normalise_entries(data)
    previous_entries = load_previous_snapshot(destination)

    current_entries = _reuse_existing_ids(current_entries, previous_entries)
    merged_entries = (
        _merge_with_previous_snapshot(current_entries, previous_entries)
        if retain_removed_entries
        else current_entries
    )

    _write_yaml(_prune_for_yaml(merged_entries), destination)

    if delta_destination is not None:
        delta_destination = _build_dated_delta_path(delta_destination, timestamp)
        delta_report = build_delta_report(
            previous_entries,
            current_entries,
            classify_missing_as_removed=not retain_removed_entries,
        )
        delta_report["generated_at"] = timestamp.isoformat()
        write_delta_report(delta_destination, delta_report)

    secho("Converted successfully to ", fg="green", nl=False)
    secho(f" {destination}", fg="yellow", bold=True)
