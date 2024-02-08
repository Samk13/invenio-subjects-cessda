# invenio-subjects-cessda

![Tests](https://github.com/Samk13/invenio-subjects-cessda/actions/workflows/tests.yaml/badge.svg)

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

Last updated: `2024-02-01`
Check the version date in this README. To fetch the latest CESSDA versions, run:

```bash
make run
```

in [config.py](invenio_subjects_cessda/config.py) you have the ability to modify the preferred language and specify the directory for saving vocabularies.
The endpoint `fullListOfpublishedVocabVersions` includes a full list of all published vocabulary versions enabling you to compare them with the versions that have been installed.

The following vocabulary versions are included in this release. Remember to update this list during your next upgrade.

```console
https://vocabularies.cessda.eu/v2/codes/CdcPublisherNames/6.0.0/en
https://vocabularies.cessda.eu/v2/codes/CessdaPersistentIdentifierTypes/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/CountryNamesAndCodes/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/TopicClassification/4.2.2/en
https://vocabularies.cessda.eu/v2/codes/AggregationMethod/1.1.2/en
https://vocabularies.cessda.eu/v2/codes/AnalysisUnit/2.1.3/en
https://vocabularies.cessda.eu/v2/codes/CharacterSet/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/CommonalityType/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/ContributorRole/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/DataSourceType/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/DataType/1.1.2/en
https://vocabularies.cessda.eu/v2/codes/DateType/1.1.2/en
https://vocabularies.cessda.eu/v2/codes/GeneralDataFormat/2.0.3/en
https://vocabularies.cessda.eu/v2/codes/LanguageProficiency/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/LifecycleEventType/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/ModeOfCollection/4.0.3/en
https://vocabularies.cessda.eu/v2/codes/NumericType/1.1.0/en
https://vocabularies.cessda.eu/v2/codes/ResponseUnit/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/SamplingProcedure/1.1.4/en
https://vocabularies.cessda.eu/v2/codes/SoftwarePackage/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/SummaryStatisticType/2.1.2/en
https://vocabularies.cessda.eu/v2/codes/TimeMethod/1.2.3/en
https://vocabularies.cessda.eu/v2/codes/TimeZone/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/TypeOfAddress/1.1.0/en
https://vocabularies.cessda.eu/v2/codes/TypeOfConceptGroup/1.0.2/en
https://vocabularies.cessda.eu/v2/codes/TypeOfFrequency/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/TypeOfInstrument/1.1.2/en
https://vocabularies.cessda.eu/v2/codes/TypeOfNote/1.1.0/en
https://vocabularies.cessda.eu/v2/codes/TypeOfTelephone/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/TypeOfTranslationMethod/1.0.0/en
https://vocabularies.cessda.eu/v2/codes/Variables-Relations/1.0.0/en
```

## Upload to pypi

Publishing will be done automatically by GitHub actions when a new tag is created.

```bash
git tag vX.Y.Z
git push origin master vX.Y.Z
```

## manually upload to pypi

```bash
make install-package-tools # this will install twine (install-package-tools-pipenv if you use pipenv)
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks

export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-<YOUR_TOKEN>
twine upload dist/*
```
