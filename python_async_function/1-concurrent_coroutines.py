#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""


import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays n ascending order
    without using sort() because of concurrency"""
    the_list = []
    delays = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*delays)
    the_list.extend(results)
    for i in range(len(the_list)):
        for k in range(0, len(the_list) - i - 1):
            if the_list[k] > the_list[k + 1]:
                the_list[k], the_list[k + 1] = the_list[k + 1], the_list[k]

    return the_list
