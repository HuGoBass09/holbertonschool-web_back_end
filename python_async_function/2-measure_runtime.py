#!/usr/bin/env python3

"""Using pyhton asyncio and random packages"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the total execution time for and returns
    avarage time elapsed for each wait_random function
    """

    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    return (end_time - start_time) / n
