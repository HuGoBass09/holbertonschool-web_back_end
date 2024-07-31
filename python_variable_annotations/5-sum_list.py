#!/usr/bin/env python3


"""A simple Python module with type annotations."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function to calculate sum of elements in a float list"""
    return sum(input_list)
