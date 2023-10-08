#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request


Auth = __import__('auth').Auth


class BasicAuth(Auth):
    pass
