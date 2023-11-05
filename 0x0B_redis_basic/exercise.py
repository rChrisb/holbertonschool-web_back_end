#!/usr/bin/env python3
"""redis basic"""


import redis
from typing import Optional, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wraps method"""
        key = method.__qualname__

        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result

    return wrapper

def call_history(method: Callable) -> Callable:
    """ call_history method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper method"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result

    return wrapper
class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:

        key = "some_random_key"

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
    
def replay(method: Callable):
    """Display the history of calls of a particular function."""
    calls_count = method.__self__._redis.get(
        method.__qualname__).decode("utf-8")
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"
    inputs_list = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs_list = method.__self__._redis.lrange(outputs_key, 0, -1)

    print(f"{method.__qualname__} was called {calls_count} times:")
    for i, (input_args, output) in enumerate(zip(inputs_list, outputs_list)):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}")


