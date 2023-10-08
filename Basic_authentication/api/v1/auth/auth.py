#!/usr/bin/env python3
""" Module of Index views
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a path."""
        if not path or not excluded_paths:
            return True

        # Add a trailing slash to the path for consistency
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]  # Remove trailing slash

            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user based on the request."""
        return None
