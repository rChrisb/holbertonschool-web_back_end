#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request
import base64
from api.v1.models.user import User
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_credentials = decoded_base64_authorization_header.split(':', 1)
        return tuple(user_credentials)

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
