"""Packaging-level assertions for invenio_subjects_cessda."""

from importlib import resources

import invenio_subjects_cessda


def test_vocabularies_bundle_contains_yaml():
    """Ensure the packaged vocabularies bundle ships the core YAML file."""
    vocab_dir = resources.files(invenio_subjects_cessda) / "vocabularies"
    yaml_file = vocab_dir.joinpath("cessda_voc.yaml")
    assert yaml_file.is_file()
    assert yaml_file.read_text(encoding="utf-8")
