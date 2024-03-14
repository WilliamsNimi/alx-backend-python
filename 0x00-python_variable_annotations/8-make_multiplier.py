#!/usr/bin/env python3
""" This is a complex types Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
