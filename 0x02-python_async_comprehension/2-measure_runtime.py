#!/usr/bin/env python3
""" This is an async time measure module """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ This is an runtime measurement function
    Return: returns the total runtime
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed_time = time.perf_counter() - start_time
    return (elapsed_time)
