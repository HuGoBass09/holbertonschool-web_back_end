#!/usr/bin/env python3

"""Python pagination"""


def index_range(page: int, page_size: int) -> tuple[int]:
    """A function to return index range"""
    if page > 0 and page_size > 0:
        return ((page - 1) * page_size, page * page_size)


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A function to get appropriate pages"""
        assert page > 0 and page_size > 0

        dataset: List = self.dataset()
        page_start, page_end = index_range(page, page_size)
        if page_end > len(dataset):
            return []
        else:
            return dataset[page_start:page_end]
