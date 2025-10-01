#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from unittest.mock import patch

from invenio_subjects_cessda.fetch_voc import fetch_voc
from tests.data import urls_to_fetch

# Sample data to mock response from the API
mock_response_data = [
    {"name": "sample_voc1", "data": {"key": "value"}},
    {"name": "sample_voc2", "data": {"key": "value"}},
]


def test_fetch_voc():
    """Test fetch_voc function."""

    async def mock_json():
        return {"key": "value"}

    class MockResponse:
        def __init__(self):
            self.json = mock_json

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    with patch("aiohttp.ClientSession.get") as mock_session_get:
        mock_session_get.return_value = MockResponse()
        fetch_res = fetch_voc(urls_to_fetch)
        assert len(fetch_res) == len(urls_to_fetch)
        # Check that all results have the expected structure
        for item in fetch_res:
            assert "name" in item
            assert "data" in item
            assert item["data"] == {"key": "value"}
