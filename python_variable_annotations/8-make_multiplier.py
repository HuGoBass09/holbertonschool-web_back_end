#!/usr/bin/env python3


"""A simple Python module with type annotations."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a multiplier function"""
    def multiplier_function(x: float) -> float:
        return multiplier * x

    return multiplier_function
