#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        # Check if authorization_header is None or not a string
        if authorization_header is None:
            return None
        if authorization_header is not isinstance(authorization_header, str):
            return None

        # Check if authorization_header starts with 'Basic ' (with a space)
        if not authorization_header.startswith('Basic '):
            return None

        # Extract the Base64 part after 'Basic '
        base64_part = authorization_header.split(' ')[1]

        return base64_part
