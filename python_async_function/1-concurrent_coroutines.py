#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""


import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    the_list = []
    delays = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*delays)
    the_list.extend(results)
    the_list.sort()

    return the_list
