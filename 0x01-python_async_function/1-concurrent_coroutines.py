#!/usr/bin/env python3
""" Concurrent coroutines """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """ This function explores concurrency
    @n: Number of times to call the async wait_random function
    @max_delay: integer meant as parameter for the async calls
    Return: Returns a list of delays from wait_random
    """
    delays = []
    for x in range(0, n):
        delays.append(await wait_random(max_delay))

    return (delays)
