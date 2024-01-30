# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.config import en_vocabularies_path, urls
from invenio_subjects_cessda.convert import convert_voc
from invenio_subjects_cessda.fetch_voc import fetch_voc


def main():
    """main entry point"""
    convert_voc(fetch_voc(urls), str(en_vocabularies_path))


if __name__ == "__main__":
    main()
