#!/usr/bin/python3
""" FIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """caching system that inherits from basecaching"""
    
    def __init__(self):
        super().__init__()
        self.list = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_to_remove = self.list.pop(0)
            del self.cache_data[key_to_remove]
            print(f"DISCARD: {key_to_remove}")
        self.cache_data[key] = item
        self.list.append(key)

        def get(self, key):
            """Get an item by key"""
            if key is None or key not in self.cache_data.keys():
                return None
        return self.cache_data[key]