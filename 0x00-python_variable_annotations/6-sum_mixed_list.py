#!/usr/bin/env python3
""" This is a complex types Module"""


def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    sum = 0
    for x in mxd_lst:
        sum += x
    return sum
