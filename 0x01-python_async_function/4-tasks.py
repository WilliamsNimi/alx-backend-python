#!/usr/bin/env python3
""" Concurrent coroutines """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[floats]:
    """ This function explores concurrency
    @n: Number of times to call the async wait_random function
    @max_delay: integer meant as parameter for the async calls
    Return: Returns a list of delays from task_wait_random
    """
    delays = []
    for x in range(0, n):
        delays.append(await task_wait_random(max_delay))

    return (delays)
