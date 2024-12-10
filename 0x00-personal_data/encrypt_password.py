#!/usr/bin/env python3
"""This module contains a function that hashes a password using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """This function hashes a password using bcrypt

    Args:
        password (str): The password to be hashed

    Returns:
        bytes: The hashed password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
