#!/usr/bin/env python3

import redis
from typing import Optional, Callable, Union

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key (e.g., using uuid)
        key = "some_random_key"  # Replace this with your key generation logic

        # Store the input data in Redis using the random key
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
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


