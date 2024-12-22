#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from bcrypt import gensalt, hashpw


def _hash_password(password: str) -> bytes:
    """This method should take in a string password and return the hashed
    version of it using bcrypt.
    """
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)
