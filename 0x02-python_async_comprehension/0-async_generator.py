#!/usr/bin/env python3
""" This is an async random number generator """
import asyncio
import random


async def async_generator():
    """ This is an async random number generator function
    Return: Generates a list of random numbers
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
