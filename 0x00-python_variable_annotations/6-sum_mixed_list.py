#!/usr/bin/env python3
""" This is a complex types Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ this is a mixed list function
    @mxd_lst: A mixed list of numbers to be summed
    Return: Returns the sum of the numbers
    """
    return float(sum(mxd_lst))
