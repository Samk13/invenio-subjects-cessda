# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

test_data = [
    {
        "id": 8812,
        "uri": "http://rdf-vocabulary.ddialliance.org/cv/TypeOfAddress/1.1/[CODE]",
        "notation": "Mailing",
        "title": "Mailing address",
        "definition": 'Includes both "street"',
        "previousConcept": 3535,
        "position": 0,
        "deprecated": False,
    },
    {
        "id": 14131,
        "uri": "https://vocabularies.cessda.eu/vocabulary/TopicClassification_[CODE]?v=4.2",
        "notation": "Health.SignsAndSymptomsPathologicalConditions",
        "title": "Signs and symptoms; pathological conditions",
        "definition": "Data on abnormal anatomical or physiological conditions",
        "previousConcept": 8961,
        "parent": "Health",
        "position": 26,
        "deprecated": False,
    },
]

res_data = [
    "https://vocabularies.cessda.eu/vocabulary/TypeOfAddress_Mailing?v=1.1&id=8812",
    "https://vocabularies.cessda.eu/vocabulary/TopicClassification_SignsAndSymptomsPathologicalConditions?v=4.2&id=14131",
]

expected_schema = [
    {
        "id": "https://vocabularies.cessda.eu/vocabulary/TypeOfAddress_Mailing?v=1.1&id=8812",
        "scheme": "CESSDA",
        "subject": "Mailing address",
    }
]

urls_to_fetch = [
    {
        "name": "Aggregation Method",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/aggregationmethod/1.1/en",
    },
    {
        "name": "Analysis Unit",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/analysisunit/2.1/en",
    },
    {
        "name": "CDC Publisher Names",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/cdcPublishernames/5.0/en",
    },
    {
        "name": "CESSDA Persistent Identifier Types",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CESSDAPersistentIdentifierTypes/1.0/en",
    },
    {
        "name": "CESSDA Topic Classification",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/topicclassification/4.2/en",
    },
    {
        "name": "Character Set",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CharacterSet/1.0/en",
    },
    {
        "name": "Commonality Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CommonalityType/1.0/en",
    },
    {
        "name": "Contributor Role",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/ContributorRole/1.0/en",
    },
    {
        "name": "Country Names and Codes",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CountryNamesandCodes/1.0/en",
    },
    {
        "name": "Data Source Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/DataSourceType/1.0/en",
    },
    {
        "name": "Data Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/DataType/1.1/en",
    },
    {
        "name": "Date Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/DateType/1.1/en",
    },
    {
        "name": "General Data Format",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/GeneralDataFormat/2.0/en",
    },
    {
        "name": "Language Proficiency",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/LanguageProficiency/1.0/en",
    },
    {
        "name": "Lifecycle Event Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/LifecycleEventType/1.0/en",
    },
    {
        "name": "Mode Of Collection",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/ModeOfCollection/4.0/en",
    },
    {
        "name": "Numeric Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/NumericType/1.1/en",
    },
    {
        "name": "Response Unit",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/ResponseUnit/1.0/en",
    },
    {
        "name": "Sampling Procedure",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/samplingprocedure/1.1/en",
    },
    {
        "name": "Software Package",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/SoftwarePackage/1.0/en",
    },
    {
        "name": "Summary Statistic Type",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/SummaryStatisticType/2.1/en",
    },
    {
        "name": "Time Method",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TimeMethod/1.2/en",
    },
    {
        "name": "Time Zone",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TimeZone/1.0/en",
    },
    {
        "name": "Type of Address",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TypeofAddress/1.1/en",
    },
    {
        "name": "Type of Concept Group",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TypeofConceptGroup/1.0/en",
    },
    {
        "name": "Type of Instrument",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TypeofInstrument/1.1/en",
    },
    {
        "name": "Type of Note",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TypeofNote/1.1/en",
    },
    {
        "name": "Type of Telephone",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TypeofTelephone/1.0/en",
    },
    {
        "name": "Type of Translation Method",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/TypeofTranslationMethod/1.0/en",
    },
    {
        "name": "rexconcepts",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/rexconcepts/1.4.0/en",
    },
]

vocabularies_published_versions_input = [
    {
        "name": "all vocabularies versions and languages",
        "data": {
            "CESSDA": {
                "CdcPublisherNames": {
                    "en(SL)": {
                        "1.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/1.0.0?languageVersion=en-1.0.0",
                        "2.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/2.0.0?languageVersion=en-2.0.0",
                        "3.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/3.0.0?languageVersion=en-3.0.0",
                        "4.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/4.0.0?languageVersion=en-4.0.0",
                        "5.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/5.0.0?languageVersion=en-5.0.0",
                        "5.0.1": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/5.0.0?languageVersion=en-5.0.1",
                        "6.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CdcPublisherNames/6.0.0?languageVersion=en-6.0.0",
                    }
                },
                "CessdaPersistentIdentifierTypes": {
                    "en(SL)": {
                        "1.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CessdaPersistentIdentifierTypes/1.0.0?languageVersion=en-1.0.0"
                    }
                },
                "CountryNamesAndCodes": {
                    "en(SL)": {
                        "1.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/CountryNamesAndCodes/1.0.0?languageVersion=en-1.0.0"
                    }
                },
                "DDI Alliance": {
                    "AggregationMethod": {
                        "en(SL)": {
                            "1.0.0": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.0.0?languageVersion=en-1.0.0",
                            "1.1.0": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.1.0?languageVersion=en-1.1.0",
                            "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.1.0?languageVersion=en-1.1.2",
                        },
                        "da(TL)": {
                            "1.1.1": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.1.0?languageVersion=da-1.1.1",
                            "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.1.0?languageVersion=da-1.1.2",
                        },
                        "no(TL)": {
                            "1.1.1": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.1.0?languageVersion=no-1.1.1",
                            "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/AggregationMethod/1.1.0?languageVersion=no-1.1.2",
                        },
                    },
                    "en(SL)": {
                        "1.1.0": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=en-1.1.0",
                        "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=en-1.1.2",
                    },
                    "da(TL)": {
                        "1.1.1": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=da-1.1.1",
                        "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=da-1.1.2",
                    },
                    "et(TL)": {
                        "1.1.1": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=et-1.1.1",
                        "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=et-1.1.2",
                    },
                    "no(TL)": {
                        "1.1.1": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=no-1.1.1",
                        "1.1.2": "http://vocabularies.cessda.eu/v2/vocabularies/DateType/1.1.0?languageVersion=no-1.1.2",
                    },
                },
            },
        },
    }
]


vocabularies_published_expected_output = [
    {
        "name": "CESSDA - CdcPublisherNames",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CdcPublisherNames/6.0.0/en",
    },
    {
        "name": "CESSDA - CessdaPersistentIdentifierTypes",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CessdaPersistentIdentifierTypes/1.0.0/en",
    },
    {
        "name": "CESSDA - CountryNamesAndCodes",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/CountryNamesAndCodes/1.0.0/en",
    },
    {
        "name": "CESSDA - DDI Alliance",
        "endpoint": "https://vocabularies.cessda.eu/v2/codes/DateType/1.1.2/en",
    },
]
