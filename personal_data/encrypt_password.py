#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """A function which returns hashed, salted password"""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """A function to check whether a password is valid or not"""
    return bcrypt.checkpw(password.encode(), hashed_password)
