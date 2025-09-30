#
# Copyright (C) 2022-2025 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Utilities for tracking vocabulary deltas between releases."""

import json
from collections.abc import Iterable
from pathlib import Path

import yaml

Snapshot = list[dict]


def load_previous_snapshot(path: Path) -> Snapshot:
    """Load the previously generated vocabulary snapshot from YAML."""
    if not path.exists():
        return []

    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or []

    if not isinstance(data, list):
        raise ValueError("Expected list of vocabulary entries in YAML snapshot")

    return data


def _index_by_id(entries: Iterable[dict]) -> dict[str, dict]:
    return {entry["id"]: entry for entry in entries}


def build_delta_report(
    previous: Snapshot,
    current: Snapshot,
    *,
    classify_missing_as_removed: bool = True,
) -> dict:
    """Compute a delta report highlighting added/removed/changed entries.

    Parameters
    ----------
    classify_missing_as_removed:
        When ``True`` (default) entries absent from the current payload are
        reported as ``removed``. When ``False`` they are tracked as
        ``omitted_from_latest`` to reflect that they remain in the exported
        vocabulary snapshot.
    """
    previous_index = _index_by_id(previous)
    current_index = _index_by_id(current)

    previous_ids = set(previous_index)
    current_ids = set(current_index)

    added_ids = current_ids - previous_ids
    removed_ids = previous_ids - current_ids
    candidate_changes = previous_ids & current_ids

    added = [_as_delta_record(entry) for entry in current if entry["id"] in added_ids]
    removed = [
        _as_delta_record(entry) for entry in previous if entry["id"] in removed_ids
    ]

    changed: list[dict] = []
    for vocab_id in sorted(candidate_changes):
        previous_entry = previous_index[vocab_id]
        current_entry = current_index[vocab_id]
        diff = _diff_entry(previous_entry, current_entry)
        if diff:
            changed.append(diff)

    summary_missing_key = (
        "removed" if classify_missing_as_removed else "omitted_from_latest"
    )

    summary = {
        "total": len(current_index),
        "added": len(added),
        summary_missing_key: len(removed),
        "changed": len(changed),
    }

    report: dict[str, object] = {
        "summary": summary,
        "added": added,
    }

    if classify_missing_as_removed:
        report["removed"] = removed
    else:
        report["omitted_from_latest"] = removed

    report["changed"] = changed
    return report


def _as_delta_record(entry: dict) -> dict:
    return {
        "id": entry.get("id"),
        "subject": entry.get("subject"),
        "scheme": entry.get("scheme"),
    }


def _diff_entry(previous: dict, current: dict) -> dict | None:
    mutations = {}
    for field in ("subject", "scheme"):
        before = previous.get(field)
        after = current.get(field)
        if before != after:
            mutations[field] = {"from": before, "to": after}

    if not mutations:
        return None

    payload = _as_delta_record(current)
    payload["changes"] = mutations
    return payload


def write_delta_report(path: Path, report: dict) -> None:
    """Persist a JSON delta report to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
