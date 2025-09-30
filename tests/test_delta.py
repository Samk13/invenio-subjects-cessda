#
# Copyright (C) 2025 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Tests for vocabulary delta tracking utilities."""

import yaml

from invenio_subjects_cessda.delta import build_delta_report, load_previous_snapshot


def test_build_delta_report_handles_added_and_changed_entries():
    previous = [
        {"id": "1", "subject": "Old subject", "scheme": "CESSDA"},
    ]
    current = [
        {"id": "1", "subject": "New subject", "scheme": "CESSDA", "vocabulary": "Voc"},
        {"id": "2", "subject": "Another", "scheme": "CESSDA", "vocabulary": "Voc"},
    ]

    delta = build_delta_report(previous, current)

    assert delta["summary"] == {"total": 2, "added": 1, "removed": 0, "changed": 1}
    assert "omitted_from_latest" not in delta["summary"]
    assert delta["added"][0]["id"] == "2"
    assert delta["changed"][0]["changes"]["subject"] == {
        "from": "Old subject",
        "to": "New subject",
    }


def test_build_delta_report_marks_missing_entries_when_retained():
    previous = [
        {"id": "1", "subject": "Legacy", "scheme": "CESSDA"},
    ]
    current = []

    delta = build_delta_report(previous, current, classify_missing_as_removed=False)

    assert delta["summary"] == {
        "total": 0,
        "added": 0,
        "omitted_from_latest": 1,
        "changed": 0,
    }
    assert "removed" not in delta["summary"]
    assert delta["omitted_from_latest"][0]["subject"] == "Legacy"


def test_load_previous_snapshot(tmp_path):
    snapshot = [{"id": "1", "subject": "Example", "scheme": "CESSDA"}]
    destination = tmp_path / "snapshot.yaml"
    destination.write_text(yaml.safe_dump(snapshot))

    loaded = load_previous_snapshot(destination)
    assert loaded == snapshot
