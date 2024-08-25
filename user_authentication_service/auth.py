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

    def create_session(self, email: str) -> str:
        """A function which creates a session ID for a user"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """A function which return a corresponding user or None"""
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """A method which deletes a user from db"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return

    def get_reset_password_token(self, email: str) -> str:
        """A method which generates reset_token"""
        try:
            user = self._db.find_user_by(email=email)
            new_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=new_token)
        except Exception:
            raise ValueError
