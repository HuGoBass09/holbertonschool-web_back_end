#!/usr/bin/env python3
""" Caching implementation """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """A function to add an element to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lru_item = self.lru_keys.pop(0)
                print(f"DISCARD: {lru_item}")
                self.cache_data.pop(lru_item)

            if key in self.lru_keys:
                self.lru_keys.remove(key)

            self.lru_keys.append(key)

    def get(self, key):
        """A function to get an item using the given key"""
        if key in self.cache_data:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return self.cache_data[key]
