#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Union, Tuple, List


num = Union[int, float]


def to_kv(k: str, v: List[num]) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, float(v ** 2))
