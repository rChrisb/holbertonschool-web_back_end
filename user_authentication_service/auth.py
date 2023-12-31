#!/usr/bin/env python3
"""hash password"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """returns a string in bytes"""

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """user registration"""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)

            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        "login validation"
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """session creation"""
        try:

            user = self._db.find_user_by(email=email)

            session_id = _generate_uuid()
            user.session_id = session_id

            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        "find user by session id"
        try:
            if session_id is not None:
                user = self._db.find_user_by(session_id=session_id)
                return user
        except NoResultFound:
            pass
        return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session"""
        try:
            user = self._db.find_user_by(id=user_id)
            if user:
                user.session_id = None
                self._db._session.commit()
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """get reset password token"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User not found")

        reset_token = str(uuid.uuid4())
        user.reset_token = reset_token
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            hashed_password = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=hashed_password,
                                 reset_token=None)


def _generate_uuid() -> str:
    """Generate and return a new UUID as a string."""
    return str(uuid.uuid4())
