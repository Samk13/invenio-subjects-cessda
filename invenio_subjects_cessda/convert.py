# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.


# from typing import Any, Callable, Dict, Iterator, NoReturn


from click import secho
from yaml import dump

from invenio_subjects_cessda.schemas import cessda_schema
from invenio_subjects_cessda.utils import logger


def sort_vocabularies(data):
    """Sort vocabularies by 'id'."""
    logger.debug("Sorting ...")
    return sorted(
        [(v["name"], s) for v in data for s in v["data"]], key=lambda x: x[1]["id"]
    )


def process_vocabularies(sorted_vocabularies):
    """Process sorted vocabularies."""
    logger.debug("Processing schema ...")
    return [
        cessda_schema((name, entry))
        for name, entry in sorted_vocabularies
        if cessda_schema((name, entry))
    ]


def write_to_file(processed_data, dpath):
    """Write processed data to a file."""
    logger.debug("Writing to: '%s'", dpath)
    with open(dpath, "w", encoding="utf-8") as yaml_f:
        for data in processed_data:
            dump(data, yaml_f, allow_unicode=True, sort_keys=False)


def log_conversion_success(dpath):
    """Log success message."""
    secho("Converted successfully to ", fg="green", nl=False)
    secho(f" {dpath}", fg="yellow", bold=True)


def convert_vocabularies(data, dpath):
    """Convert vocabularies to yaml."""
    logger.debug("Convert vocabularies started ...")
    sorted_vocabularies = sort_vocabularies(data)
    processed_data = process_vocabularies(sorted_vocabularies)
    write_to_file(processed_data, dpath)
    log_conversion_success(dpath)
