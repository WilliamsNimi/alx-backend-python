#!/usr/bin/env python3
""" This is an async comprehension module """
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This is an async comprehension function
    Return: returns 10 random Numbers
    """
    return ([i async for i in async_generator()])
