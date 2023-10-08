#!/usr/bin/env python3
"""
Main file
"""


import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    regex = re.compile(r'(' + '|'.join(
        re.escape(field) for field in fields) + r')=[^' + separator + r']*')
    return regex.sub(f'\\1={redaction}', message)
