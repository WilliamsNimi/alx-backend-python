#!/usr/bin/env python3
""" Measuring Run Time """


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ This function explores measuring run time
    @n: Number of times to call the async wait_random function
    @max_delay: integer meant as parameter for the async calls
    Return: Returns time per call
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time

    return (elapsed_time / n)
