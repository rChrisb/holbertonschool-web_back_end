#!/usr/bin/env python3
"""Complex types - mixed list"""


from typing import List, Union


num = Union[int, float]


def sum_mixed_list(mxd_lst: List[num]) -> float:
    """takes a list mxd_lst of integers and floats
    and returns their sum as a float"""
    return sum(mxd_lst)
