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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This function checks if a password is valid

    Args:
        hashed_password (bytes): The hashed password
        password (str): The password to be checked

    Returns:
        bool: True if the password is valid, False otherwise
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
