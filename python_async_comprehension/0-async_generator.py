#!/usr/bin/env python3

"""A function that uses async comprehension"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator that yields random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
