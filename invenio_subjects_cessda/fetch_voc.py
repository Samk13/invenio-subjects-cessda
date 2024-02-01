# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology Sweden.
#
# invenio-subjects-CESSDA is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.


from asyncio import gather, run

from aiohttp import ClientSession

from invenio_subjects_cessda.utils import logger


# Data fetching
async def fetch(session, url_obj):
    """Fetch API calls."""
    logger.debug("Making request to '%s'", url_obj["endpoint"])
    try:
        async with session.get(url_obj["endpoint"]) as res:
            data = await res.json()
            return {"name": url_obj["name"], "data": data}
    except Exception as e:
        logger.error("Error fetching %s: %s", url_obj["name"], e)
        return None


async def gather_data(urls):
    """Gather workers."""
    async with ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await gather(*tasks, return_exceptions=True)
        return [result for result in results if result is not None]


def fetch_voc(urls):
    """Fetch CESSDA voc and return a list."""
    return run(gather_data(urls))
