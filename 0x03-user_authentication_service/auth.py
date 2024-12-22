#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from bcrypt import gensalt, hashpw
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """This method should take in a string password and return the hashed
    version of it using bcrypt.
    """
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)


""" Task 5"""


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """This method should allow a user to register by providing an email
        and password. It should then call the _hash_password method
        to securely store the user's password in the database.
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(
                f"User {user.email} already exists"
            )
        except NoResultFound:
            return self._db.add_user(
                email, str(_hash_password(password))
            )
