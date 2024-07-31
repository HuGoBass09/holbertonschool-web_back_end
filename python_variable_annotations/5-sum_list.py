#!/usr/bin/env python3
from typing import List

"""A simple Python module with type annotations."""


def sum_list(input_list: List[float]) -> float:
    """A function to calculate sum of elements in a float list"""
    sum = 0
    for items in input_list:
        sum += items
    return sum
