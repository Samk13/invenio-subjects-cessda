#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.writer import write_voc
from tests.data import test_data


def test_write_voc(create_json_path):  # noqa: F811
    """Test write json"""
    voc_path = create_json_path
    write_voc(voc_path, test_data, "w+")
    with open(voc_path, encoding="utf-8") as f:
        data = f.read()
        assert len(data) > 0
