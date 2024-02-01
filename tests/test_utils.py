# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.config import languages
from invenio_subjects_cessda.utils import fix_url, get_latest_versions
from tests.data import (
    res_data,
    test_data,
    vocabularies_published_expected_output,
    vocabularies_published_versions_input,
)


def test_fix_url():
    """Test fix_url."""
    for i, u in enumerate(test_data):
        assert fix_url(u) == res_data[i]


def test_get_latest_versions():
    """Test get latest versions for api URLs."""
    result = get_latest_versions(vocabularies_published_versions_input, languages)
    assert result == vocabularies_published_expected_output
