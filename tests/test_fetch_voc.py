# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from unittest.mock import MagicMock, patch

import pytest

from invenio_subjects_cessda.fetch_voc import fetch_voc
from tests.data import urls_to_fetch

# Sample data to mock response from the API
mock_response_data = [
    {"name": "sample_voc1", "data": {"key": "value"}},
    {"name": "sample_voc2", "data": {"key": "value"}},
]


@pytest.mark.asyncio
async def test_fetch_voc():
    """Test fetch_voc function."""

    async def mock_json():
        return {"key": "value"}

    async def mock_get():
        mock_resp = MagicMock()
        mock_resp.json = mock_json
        return mock_resp

    with patch("aiohttp.ClientSession.get", new=mock_get):
        fetch_res = await fetch_voc(urls_to_fetch)
        assert len(fetch_res) == len(urls_to_fetch)
        for item in fetch_res:
            assert item in mock_response_data
