#!/usr/bin/env python3
""" This is a complex types Module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This is a type function for tuples
    @k: A string to be returned after an operation
    @v: A number that can be either a float or an int
    Return: Returns a tuple of k and v squared
    """
    return (k, v**2)
