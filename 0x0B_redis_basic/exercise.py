#!/usr/bin/env python3

import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        # Initialize the Redis client
        self._redis = redis.Redis()
        # Flush the database to start fresh
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the data in Redis with the random key
        self._redis.set(key, data)
        # Return the generated key
        return key
