#!/usr/bin/env python3
""" Caching implementation """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def put(self, key, item):
        """A function to add an element to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                last_item = list(self.cache_data.keys())[len(self.cache_data) - 1]
                print(f"DISCARD: {last_item}\n")
                self.cache_data.pop(last_item)

    def get(self, key):
        """A function to get an item using the given key"""
        if key in self.cache_data:
            return self.cache_data[key]
