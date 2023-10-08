#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request
import base64


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:

        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.lower().startswith('basic '):
            return None

        base64_part = authorization_header.split(' ')[1]

        return base64_part
