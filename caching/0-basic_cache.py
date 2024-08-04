#!/usr/bin/env python3
""" Caching implementation """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key, item):
        """A function to add an element to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """A function to get an item using the given key"""
        if key in self.cache_data:
            return self.cache_data[key]
