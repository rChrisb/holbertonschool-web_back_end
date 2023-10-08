#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request
import base64


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits from auth"""
    def extract_base64_authorization_header(self, authorization_header: str
                                            ) -> str:
        """returns the Base64 part of the Authorization header"""

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.lower().startswith('basic '):
            return None

        base64_part = authorization_header.split(' ')[1]

        return base64_part

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None
