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
            return bcrypt.checkpw(password.encode("utf-8"),
                                  obj.hashed_password)
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

    """ Task 12 """

    def get_user_from_session_id(self, session_id: str) -> str:
        """This method should check the session ID provided and return
        the user's email address.
        But if the session ID is invalid, it should return None.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The user's email address.
        """
        try:
            obj = self._db.find_user_by(session_id=session_id)
            return obj.email
        except Exception:
            return None

    """ Task 13 """

    def destroy_session(self, user_id: int):
        """

        Args:
            user_id (int): _description_

        Returns:
            _type_: _description_
        """
        obj = self._db.find_user_by(id=user_id)
        obj.session_id = None
        return None

    """ Task 16 """

    def get_reset_password_token(self, email: str) -> str:
        """This method should generate a reset password token and update
        the user's reset_token attribute with it. It should then return
        the reset password token.

        Args:
            email (str): The user's email address.

        Returns:
            str: The reset password token.
        """
        try:
            obj = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            obj.reset_token = reset_token
            se = self._db._session
            se.commit()

            return reset_token
        except Exception:
            raise ValueError()

    """ Task 18 """

    def update_password(self, reset_token: str, password: str) -> None:
        """This method should update the user's
        password with the provided reset
        token and password.

        Args:
            reset_token (str): The reset token
            password (str): The new password
        """
        try:
            obj = self._db.find_user_by(reset_token=reset_token)
            if obj:
                new_pwd = hashpw(password.encode("utf-8"), gensalt())
                obj.hashed_password = new_pwd
                obj.reset_token = None
                return None
        except Exception:
            raise ValueError()


""" Task 9"""


def _generate_uuid() -> str:
    """This method should generate a UUID.
    """
    return str(uuid.uuid4())
