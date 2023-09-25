#!/usr/bin/env python3
"""runtime for four parallel comprehensions"""


import asyncio
import time

async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the total runtime and return it."""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    end = asyncio.get_event_loop().time()
    runtime = end - start
    return runtime
