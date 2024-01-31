# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.fetch_voc import fetch_voc
from tests.data import urls_to_fetch


# @pytest.mark.asyncio
def test_fetch_voc():
    """Test fetch_voc."""
    fetch_res = fetch_voc(urls_to_fetch)
    assert len(fetch_res) == len(urls_to_fetch)
