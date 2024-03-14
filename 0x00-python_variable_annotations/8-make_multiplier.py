#!/usr/bin/env python3
""" This is a complex types Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This is a Callable type function
    @multiplier: This is a multiplier value
    Return: Returns a function that multiplies with the multiplier
    """
    return lambda x: x * multiplier
