#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    pass
