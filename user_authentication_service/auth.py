#!/usr/bin/env python3
"""hash password"""


import bcrypt


def _hash_password(self, password):

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
