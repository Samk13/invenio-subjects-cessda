#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Test subjects extension conforms to subjects extension interface."""

from importlib import metadata

from invenio_subjects_cessda import __version__


def test_version():
    """Test version import."""
    assert __version__


def test_vocabularies_yaml():
    """Test vocabularies.yaml structure."""
    entry_points = metadata.entry_points()
    if hasattr(entry_points, "select"):
        fixtures_eps = entry_points.select(group="invenio_rdm_records.fixtures")
    else:  # pragma: no cover - fallback for Python <3.10
        fixtures_eps = entry_points.get("invenio_rdm_records.fixtures", [])

    extensions = [ep.load() for ep in fixtures_eps]

    assert len(extensions) == 1
