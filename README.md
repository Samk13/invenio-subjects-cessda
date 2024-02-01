# invenio-subjects-cessda

## Overview

`invenio-subjects-cessda` is a Python package designed to integrate the CESSDA Vocabulary with [InvenioRDM](https://inveniosoftware.org/products/rdm/)
It enables indexing and retrieval of STI Repository materials using CESSDA subject terms.

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

## Upload to pypi

```bash
make install-package-tools # this will install twine (install-package-tools-pipenv if you use pipenv)
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks
twine upload -u <USERNAME> -p <PASSWORD> --repository-url https://test.pypi.org/legacy/ dist/* --verbose
# or:
twine upload --repository PROJECT_NAME
```

### Debug Log Examples

The vocabularies versions That is been included are the following:

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
