#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user based on the request."""
        return None
