#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

import json
from pathlib import Path

import yaml

from invenio_subjects_cessda.convert import convert_vocabularies
from tests.data import test_data


def _load_delta_report(base_path: Path) -> tuple[Path, dict]:
    delta_files = sorted(base_path.parent.glob(f"{base_path.stem}_*.json"))
    assert delta_files, "No timestamped delta report was generated"
    delta_file = delta_files[-1]
    with delta_file.open(encoding="utf-8") as handle:
        return delta_file, json.load(handle)


def test_convert_vov(create_yaml_path, create_delta_path):
    """Test convert_voc."""
    voc_path = Path(create_yaml_path)
    delta_path = create_delta_path
    legacy_entry = [
        {
            "id": "legacy-id",
            "scheme": "CESSDA",
            "subject": "Mailing address",
        }
    ]
    voc_path.write_text(yaml.safe_dump(legacy_entry))
    test_d = [{"data": test_data, "name": "Test name"}]
    convert_vocabularies(test_d, str(voc_path), delta_path)

    vocab_entries = yaml.safe_load(voc_path.read_text(encoding="utf-8"))
    assert isinstance(vocab_entries, list)
    assert vocab_entries[0]["subject"] <= vocab_entries[1]["subject"]
    assert vocab_entries[0]["id"] == "legacy-id"

    delta_file, delta_report = _load_delta_report(Path(delta_path))

    assert delta_file.name.startswith("delta-report_")
    assert "Z" not in delta_file.stem
    postfix = delta_file.stem.split("T")[-1]
    assert "_" in postfix
    assert list(delta_report)[0] == "summary"

    summary = delta_report["summary"]
    assert summary["total"] == len(vocab_entries)
    assert summary["added"] == 1
    assert summary["omitted_from_latest"] == 0
    assert "removed" not in summary

    assert not delta_report.get("omitted_from_latest")
    assert not delta_report["changed"]


def test_convert_retains_removed_entries(create_yaml_path, create_delta_path):
    """Removed upstream entries stay in the exported snapshot."""

    voc_path = Path(create_yaml_path)
    delta_path = create_delta_path

    legacy_entries = [
        {
            "id": "legacy-id",
            "scheme": "CESSDA",
            "subject": "Mailing address",
        },
        {
            "id": "obsolete-id",
            "scheme": "CESSDA",
            "subject": "Obsolete subject",
        },
    ]
    voc_path.write_text(yaml.safe_dump(legacy_entries), encoding="utf-8")

    convert_vocabularies(
        [{"data": test_data, "name": "Test name"}], str(voc_path), delta_path
    )

    vocab_entries = yaml.safe_load(voc_path.read_text(encoding="utf-8"))
    subjects = {entry["subject"] for entry in vocab_entries}

    assert "Obsolete subject" in subjects
    assert len(vocab_entries) == 3

    delta_file, delta_report = _load_delta_report(Path(delta_path))

    assert delta_file.name.startswith("delta-report_")
    assert "Z" not in delta_file.stem
    postfix = delta_file.stem.split("T")[-1]
    assert "_" in postfix
    assert list(delta_report)[0] == "summary"
    assert delta_report["summary"] == {
        "total": 2,
        "added": 1,
        "omitted_from_latest": 1,
        "changed": 0,
    }
    assert delta_report["omitted_from_latest"][0]["subject"] == "Obsolete subject"


def test_convert_can_drop_removed_entries(create_yaml_path, create_delta_path):
    """Optional flag prunes entries missing from the current payload."""

    voc_path = Path(create_yaml_path)
    delta_path = create_delta_path

    legacy_entries = [
        {
            "id": "legacy-id",
            "scheme": "CESSDA",
            "subject": "Mailing address",
        },
        {
            "id": "obsolete-id",
            "scheme": "CESSDA",
            "subject": "Obsolete subject",
        },
    ]
    voc_path.write_text(yaml.safe_dump(legacy_entries), encoding="utf-8")

    convert_vocabularies(
        [{"data": test_data, "name": "Test name"}],
        str(voc_path),
        delta_path,
        retain_removed_entries=False,
    )

    vocab_entries = yaml.safe_load(voc_path.read_text(encoding="utf-8"))

    subjects = {entry["subject"] for entry in vocab_entries}
    assert "Obsolete subject" not in subjects

    delta_file, delta_report = _load_delta_report(Path(delta_path))

    assert delta_file.name.startswith("delta-report_")
    assert "Z" not in delta_file.stem
    postfix = delta_file.stem.split("T")[-1]
    assert "_" in postfix
    assert list(delta_report)[0] == "summary"
    assert delta_report["summary"] == {
        "total": 2,
        "added": 1,
        "removed": 1,
        "changed": 0,
    }
    assert "omitted_from_latest" not in delta_report["summary"]
    assert "omitted_from_latest" not in delta_report
