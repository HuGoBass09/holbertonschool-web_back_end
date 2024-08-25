#!/usr/bin/env python3
"""auth module"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """A method which returns hashed and salted password string"""
    byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte, salt)
    return hashed_password


def _generate_uuid() -> str:
    """A function which returns a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """A method which registers and returns a new user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed_password = _hash_password(password).decode()
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """A method to check if a user is valid"""
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode("utf-8")
            user_password = user.hashed_password.encode("utf-8")
            return bcrypt.checkpw(password, user_password)
        except Exception:
            return False
