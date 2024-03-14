#!/usr/bin/env python3
""" This is a complex types Module"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ a sum of list function
    @input_list: The list of floats to be summed
    Return: Returns the sum of lists
    """
    return float(sum(input_list))
