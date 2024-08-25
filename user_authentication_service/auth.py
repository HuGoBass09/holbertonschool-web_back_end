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
