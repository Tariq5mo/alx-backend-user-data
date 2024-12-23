#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from bcrypt import gensalt, hashpw
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import uuid


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
                email, _hash_password(password)
            )

    """ Task 8"""

    def valid_login(self, email: str, password: str) -> bool:
        """This method checks if the email and password provided are valid
        credentials. Returns a boolean.
        """
        try:
            obj = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"), obj.hashed_password)
        except Exception:
            return False

    """ Task 10 """

    def create_session(self, email: str) -> str:
        """This method should create a new session for the user with the
        provided email. It should return the session ID.

        Args:
            email (str): The user's email address.

        Returns:
            str: The newly created session ID.
        """
        if email:
            obj = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            obj.session_id = session_id
            return session_id


""" Task 9"""


def _generate_uuid() -> str:
    """This method should generate a UUID.
    """
    return str(uuid.uuid4())
