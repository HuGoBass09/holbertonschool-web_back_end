#!/usr/bin/env python3


"""A simple Python module with type annotations."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function to calculate the sum of a mixed list"""
    return sum(mxd_lst)
