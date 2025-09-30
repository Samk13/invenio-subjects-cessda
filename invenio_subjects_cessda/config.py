#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from pathlib import Path

# languages = ["en(SL)", "sv(TL)"]
languages = ["en(SL)"]
"""Languages to fetch"""

VOCABULARY_DIR = Path.cwd() / "invenio_subjects_cessda" / "vocabularies"

en_vocabularies_output_path = VOCABULARY_DIR / "cessda_voc.yaml"
"""CESSDA vocabulary export destination."""

en_vocabularies_delta_path = VOCABULARY_DIR / "cessda_voc_delta.json"
"""Delta report file path recording vocabulary changes between runs."""


fullListOfpublishedVocabVersions = [
    {
        "name": "all vocabularies versions and languages",
        "endpoint": "https://vocabularies.cessda.eu/v2/vocabularies-published",
    }
]
"""https://api.tech.cessda.eu/#/vocabulary-resource-v-2/getAllVocabulariesUsingGET"""


# # Sort existing CESSDA vocabulary entries by subject and id
# ```python
# python3 - <<'PY'
# from pathlib import Path
# import yaml

# path = Path("invenio_subjects_cessda/vocabularies/cessda_voc.yaml")
# entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
# entries.sort(key=lambda item: (item["subject"].lower(), item["id"]))
# path.write_text(
#     yaml.safe_dump(entries, allow_unicode=True, sort_keys=False),
#     encoding="utf-8",
# )
# PY
# ```
