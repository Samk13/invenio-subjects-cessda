#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2025 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

set -o errexit
set -o nounset
set -o pipefail

echo "Validating packaging metadata with an isolated build..."
tmp_build_dir=$(mktemp -d)
cleanup() {
    rm -rf "${tmp_build_dir}"
}
trap cleanup EXIT
uvx --from build pyproject-build --sdist --wheel --outdir "${tmp_build_dir}"
trap - EXIT
cleanup

echo "Running pytest..."
uv run python -m pytest
echo "Running code quality checks with Ruff..."
uv run python -m ruff check .
uv run python -m ruff format --check .

