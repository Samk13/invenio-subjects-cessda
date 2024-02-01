# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.config import (
    en_vocabularies_output_path,
    fullListOfpublishedVocabVersions,
    languages,
)
from invenio_subjects_cessda.convert import convert_vocabularies
from invenio_subjects_cessda.fetch_voc import fetch_voc
from invenio_subjects_cessda.utils import get_latest_versions


def main():
    """main entry point"""
    all_vocabularies_published = fetch_voc(fullListOfpublishedVocabVersions)
    latest_versions_urls = get_latest_versions(all_vocabularies_published, languages)
    convert_vocabularies(
        fetch_voc(latest_versions_urls), str(en_vocabularies_output_path)
    )


if __name__ == "__main__":
    main()
