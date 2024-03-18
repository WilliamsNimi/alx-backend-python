#!/usr/bin/env python3
""" This is an async await module"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """ This function simulates async
    @max_delay: Takes a random integer with an inital value of 10
    Return: Returns a random floating point number between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
