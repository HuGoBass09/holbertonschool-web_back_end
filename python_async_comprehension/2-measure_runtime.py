#!/usr/bin/env python3
"""program that creates an async generator"""

async_comprehension = __import__("1-async_comprehension").async_comprehension

import asyncio
import time


async def measure_runtime() -> float:
    """A function to measure runtime for async_comprehension"""
    start_time = time.time()
    asyncio.gather(async_comprehension() for _ in range(4))
    end_time = time.time()
    return end_time - start_time
