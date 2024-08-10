#!/usr/bin/env python3

"""Python pagination"""


def index_range(page: int, page_size: int) -> tuple[int]:
    """A function to return index range"""
    if page > 0 and page_size > 0:
        return ((page - 1) * page_size, page * page_size)
