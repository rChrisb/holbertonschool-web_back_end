#!/usr/bin/env python3
"""User model"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User class"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __init__(self, email, hashed_password, session_id=None,
                 reset_token=None):
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token
