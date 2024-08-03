#!/usr/bin/env python3
"""A function that uses async comprehension"""

async_comprehension = __import__("1-async_comprehension").async_comprehension

import asyncio
import time


async def measure_runtime() -> float:
    """
    A function to measure runtime 
    for async_comprehension
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
