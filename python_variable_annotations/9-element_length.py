#!/usr/bin/env python3


"""A simple Python module with type annotations."""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """The given function is redefined using type annotation"""
    return [(i, len(i)) for i in lst]
