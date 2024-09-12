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
