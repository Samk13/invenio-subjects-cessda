# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from pathlib import Path

# languages = ["en(SL)", "sv(TL)"]
languages = ["en(SL)"]
"""Languages to fetch"""

en_vocabularies_output_path = (
    Path.cwd() / "invenio_subjects_cessda" / "vocabularies" / "cessda_voc.yaml"
)
"""CESSDA Vocabularies path destination"""


fullListOfpublishedVocabVersions = [
    {
        "name": "all vocabularies versions and languages",
        "endpoint": "https://vocabularies.cessda.eu/v2/vocabularies-published",
    }
]
"""https://api.tech.cessda.eu/#/vocabulary-resource-v-2/getAllVocabulariesUsingGET"""
