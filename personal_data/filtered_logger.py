#!/usr/bin/env python3
"""
Main file
"""


import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Regex-ing"""
    for field in fields:
        pattern = re.escape(field) + r'=[^' + separator + r']*'
        message = re.sub(pattern, field + '=' + redaction, message)
    return message
