#!/usr/bin/env python3


"""A simple Python module with type annotations."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function to create a tuple from two arguments"""
    return tuple(k, v**2)
