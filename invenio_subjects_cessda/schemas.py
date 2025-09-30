#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_subjects_cessda.utils import fix_url


def cessda_schema(entry):
    """Return a normalized CESSDA vocabulary record."""
    if not entry:
        return None

    subject = entry.get("title")
    if not subject:
        return None

    return {
        "id": fix_url(entry),
        "scheme": "CESSDA",
        "subject": subject.strip(),
    }
