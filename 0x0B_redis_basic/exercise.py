#!/usr/bin/env python3
"""Redis module"""

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """Cache redis class"""

    def __init__(self):
        """Constructor for the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """A method to store data into redis cache"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        """A method to get key from redis"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """A method to get a string"""
        return string.decode("utf-8")

    def get_int(self, number: bytes) -> int:
        """A method to get an integer value"""
        result = int(number)
        return result
