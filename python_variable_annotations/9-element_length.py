#!/usr/bin/env python3
"""duck type an iterable object"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """appropriate types"""
    return [(i, len(i)) for i in lst]
