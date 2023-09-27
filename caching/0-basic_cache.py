#!/usr/bin/python3
"""Basic dictionary"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching system that inherits from basecaching"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
