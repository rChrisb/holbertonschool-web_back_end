#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def inner_function(a: float) -> float:
        return a * multiplier
    return inner_function
