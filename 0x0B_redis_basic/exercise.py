#!/usr/bin/env python3

import redis
from typing import Optional, Callable

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Optional[str, bytes, int, float]) -> str:
        # Generate a random key (e.g., using uuid)
        key = "some_random_key"  # Replace this with your key generation logic

        # Store the input data in Redis using the random key
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[str, bytes, int, float]:
        # Retrieve data from Redis
        data = self._redis.get(key)

        # If the data is not found in Redis, return None
        if data is None:
            return None

        # If a conversion function (fn) is provided, apply it to the data
        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)

# Example usage:
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
