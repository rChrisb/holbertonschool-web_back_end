#!/usr/bin/env python3
"""
Main file
"""


import re


def filter_datum(fields, redaction, message, separator):
    """Regex-ing"""
    for field in fields:
        pattern = re.escape(field) + r'=[^' + separator + r']*'
        message = re.sub(pattern, field + '=' + redaction, message)
    return message
