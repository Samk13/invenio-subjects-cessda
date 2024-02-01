# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
import logging
import os
import re
from urllib.parse import urlparse

# Set up logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# Function to set the logging level based on the DEBUGGER environment variable
def configure_logging():
    """Debugger config."""
    debugger = os.getenv("DEBUGGER", "False").lower()
    if debugger == "true":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)


# Invoke it
configure_logging()


def fix_url(obj_in):
    """Fix broken urls for certain vocabularies."""
    url_in_ = urlparse(obj_in["uri"])
    netloc = url_in_.netloc
    path = url_in_.path.split("/")
    base = "https://vocabularies.cessda.eu/vocabulary"
    vcode = "".join(obj_in["notation"]).rsplit(".", maxsplit=1)[-1]

    if netloc == "rdf-vocabulary.ddialliance.org":
        return f"{base}/{path[2]}_{vcode}?v={path[3]}&id={obj_in['id']}"
    else:
        nyurl = "".join(f"{obj_in['uri']}".replace("[CODE]", vcode))
        return f"{nyurl}&id={obj_in['id']}"


def convert_url(input_url):
    """Convert url."""
    # Extracting contentType, Language and Version from the input URL
    logger.debug("convert_url_input: %s", input_url)
    match = re.search(
        r"/vocabularies/([^/]+)/[^?]+\?languageVersion=([a-z]{2})-([\d\.]+)", input_url
    )
    if match:
        content_type, language, version = match.groups()
        # Constructing the new URL
        result = f"https://vocabularies.cessda.eu/v2/codes/{content_type}/{version}/{language}"
        logger.debug("convert_url_output: %s", result)
        return result


def get_latest_versions(data, languages):
    """
    Retrieves the latest vocabularies versions.

    Args:
    data (list): List of dictionaries with name and data.
    Data is a nested dictionary with categories, languages, and versions.
    languages (list): Languages to filter versions.

    Returns:
    list: [{'name': str, 'endpoint': str}] with vocabulary name and latest version URLs.
    """
    result = []
    for item in data:

        logger.debug("Processing item: %s", item["name"])

        for provider, categories in item["data"].items():
            for category, langs in categories.items():
                for lang, versions in langs.items():
                    if lang in languages:
                        latest_version = max(
                            versions, key=lambda v: list(map(int, v.split(".")))
                        )

                        logger.debug("latest version: %s", latest_version)
                        result.append(
                            {
                                "name": f"{provider} - {category}",
                                "endpoint": convert_url(versions[latest_version]),
                            }
                        )
    logger.debug("Get latest versions for languages: '%s' completed", languages)
    return result
