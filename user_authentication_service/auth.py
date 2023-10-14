#!/usr/bin/env python3
"""hash password"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """returns a string in bytes"""

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
