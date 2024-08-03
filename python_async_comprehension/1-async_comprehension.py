#!/usr/bin/env python3

"""A function that uses async comprehension"""

async_generator = __import__("0-async_generator").async_generator

from typing import List


async def async_comprehension() -> List[float]:
    """
    A function to return 10 random numbers
    using async_comprehension
    """
    return [i async for i in async_generator()]
