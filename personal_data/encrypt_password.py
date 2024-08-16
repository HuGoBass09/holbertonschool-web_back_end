#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """A function which returns hashed, salted password"""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed_password
