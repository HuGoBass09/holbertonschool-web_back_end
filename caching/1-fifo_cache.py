#!/usr/bin/env python3
""" Caching implementation """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def put(self, key, item):
        """A function to add an element to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_item = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_item}")
                self.cache_data.pop(first_item)

    def get(self, key):
        """A function to get an item using the given key"""
        if key in self.cache_data:
            return self.cache_data[key]
