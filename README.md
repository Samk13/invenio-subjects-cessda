# invenio-subjects-cessda

![Tests](https://github.com/Samk13/invenio-subjects-cessda/actions/workflows/tests.yaml/badge.svg)
![Pypi](https://img.shields.io/pypi/v/invenio-subjects-cessda.svg)
![License](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Downloads](https://static.pepy.tech/badge/invenio-subjects-cessda)](https://pepy.tech/project/invenio-subjects-cessda)

## Overview

[CESSDA](https://www.cessda.eu/About) stands for Consortium of European Social Science Data Archives and ERIC stands for European Research Infrastructure Consortium.

CESSDA provides large-scale, integrated and sustainable data services to the social sciences. It brings together social science data archives across Europe, with the aim of promoting the results of social science research and supporting national and international research and cooperation.
`invenio-subjects-cessda` is a Python package designed to integrate the CESSDA Vocabulary with [InvenioRDM](https://inveniosoftware.org/products/rdm/)

## Installation

### Prerequisites

Active virtual environment of your InvenioRDM instance.
From your instance active venv:

### Steps

1- Install the package:

```bash
pip install invenio-subjects-cessda

```

2- Run the following commands in your InvenioRDM instance:

```console
invenio rdm-records fixtures
invenio-cli run
```

### Versioning

This project adheres to [SemVer versioning](https://semver.org/):

## Usage Guide

### For Instance Administrators

After installation:
1- Refer to [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)
2- Run the following commands:

```bash
pip install invenio-subjects-cessda
invenio rdm-records fixtures
invenio-cli run
```

Your instance is now ready to use the CESSDA vocabulary.

## For Package Maintainers

Setting Up Development Environment
After cloning the repository:

```bash
# Run make install to install dependencies.
make install
# Use make test to run tests.
make test
```

### Debugging

Modify `Makefile` to set the DEBUGGER environment variable to False for less detailed logging.

### Updating CESSDA Versions

To fetch the latest CESSDA vocabularies, run:

```bash
make run
```

You can change the preferred languages and output locations in
[config.py](invenio_subjects_cessda/config.py). The command downloads all
vocabularies, writes the canonical list to
`invenio_subjects_cessda/vocabularies/cessda_voc.yaml`, and persists a delta
report alongside it. Delta filenames now include the UTC timestamp of the run
(`cessda_voc_delta_YYYYMMDDTHH_MMSS.json`) so each execution leaves an audit
trail you can revisit for curation.

Review the delta report after each update to see which vocabularies were added,
changed, or missing from the latest upstream catalogue. When entries disappear
from the fetch but are still retained in the YAML, they are reported under the
`missing_from_latest` key so it is clear that the export still contains them. If
you run the synchronisation with removals enabled, the report switches back to
the traditional `removed` section.

Existing subjects keep their original identifiers so Invenio instances will not
create duplicate records when the upstream catalogue republishes entries with
new IDs.

To explicitly prune removed vocabularies from the YAML, call the synchronisation
script with the `--drop-removed-vocabs` flag:

```bash
make run-force-delete
# or
python main.py --drop-removed-vocabs
```

Without the flag, legacy entries remain in the export for backward
compatibility, while the delta report records that they are missing upstream.

## Upload to pypi

Publishing will be done automatically by GitHub actions when a new tag is created.

```bash
git tag vX.Y.Z
git push origin master vX.Y.Z
```
