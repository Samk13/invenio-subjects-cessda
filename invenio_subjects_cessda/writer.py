# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from json import dumps

from click import secho


def write_voc(data_file_path, res, mode="w+"):
    """Write result to disk.

    Args:
        data_file_path (str): file path
        result (arr): data arr
        mode (str): open mode
    """
    with open(data_file_path, mode, encoding="utf-8") as f:
        f.write(dumps(res, indent=2))
        secho(
            f"Data downloaded and saved successfully in: {data_file_path}", fg="green"
        )
