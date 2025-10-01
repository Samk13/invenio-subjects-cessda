#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.


import pytest


@pytest.fixture()
def create_yaml_path(tmp_path):
    """Provide a temporary YAML path."""
    path = tmp_path / "test.yaml"
    yield str(path)
    path.unlink(missing_ok=True)


@pytest.fixture()
def create_json_path(tmp_path):
    """Provide a temporary JSON path."""
    path = tmp_path / "test.json"
    yield str(path)
    path.unlink(missing_ok=True)


@pytest.fixture()
def create_delta_path(tmp_path):
    """Provide a temporary delta report path."""
    path = tmp_path / "delta-report.json"
    yield str(path)
    for file in tmp_path.glob("delta-report_*.json"):
        file.unlink(missing_ok=True)
    path.unlink(missing_ok=True)
