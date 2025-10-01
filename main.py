#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

import click

from invenio_subjects_cessda.config import (
    en_vocabularies_delta_path,
    en_vocabularies_output_path,
    fullListOfpublishedVocabVersions,
    languages,
)
from invenio_subjects_cessda.convert import convert_vocabularies
from invenio_subjects_cessda.fetch_voc import fetch_voc
from invenio_subjects_cessda.utils import get_latest_versions


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--drop-removed-vocabs",
    is_flag=True,
    default=False,
    help=(
        "Prune entries that were removed upstream instead of keeping them in the"
        " exported YAML."
    ),
)
def main(drop_removed_vocabs: bool = False) -> None:
    """Synchronise the local CESSDA vocabulary snapshot."""

    all_vocabularies_published = fetch_voc(fullListOfpublishedVocabVersions)
    latest_versions_urls = get_latest_versions(all_vocabularies_published, languages)

    convert_vocabularies(
        fetch_voc(latest_versions_urls),
        str(en_vocabularies_output_path),
        str(en_vocabularies_delta_path),
        retain_removed_entries=not drop_removed_vocabs,
    )


if __name__ == "__main__":
    main()
