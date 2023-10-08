#!/usr/bin/env python3
"""
Main file
"""


import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Regex-ing"""
    for field in fields:
        pattern = re.escape(field) + r'=[^' + separator + r']*'
        message = re.sub(pattern, field + '=' + redaction, message)
    return message
