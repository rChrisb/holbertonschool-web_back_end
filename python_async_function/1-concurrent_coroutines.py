#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""


import asyncio
import random


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list:
    list = []
    delays = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*delays)
    list.extend(results)
    list.sort()

    return list
