#!/usr/bin/env python3
"""
Basic Authentication module.
"""
from typing import List, Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """
    Basic Authentication class.
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of
        the Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The authorization header.

        Returns:
            str: The Base64 part of the authorization header,
            or None if invalid.
        """
        if authorization_header is None or not isinstance(
            authorization_header, str
        ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 part of
        the Authorization header for Basic Authentication.

        Args:
            base64_authorization_header (str):
                The Base64 authorization header.

        Returns:
            str: The decoded value as a UTF8 string, or None if invalid.
        """
        try:
            if isinstance(base64_authorization_header, str):
                decoded_str = base64.b64decode(base64_authorization_header)
                return decoded_str.decode("utf-8")
            return None
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Extracts user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
                    The decoded Base64 authorization header.

        Returns:
            Tuple[str, str]: The user email and password,
            or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"): # type: ignore
        """This method returns the User instance
        based on the email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance, or None if invalid.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            User.load_from_file()  # Ensure User data is loaded
            all_objs_email = User.search({"email": user_email})
        except KeyError:
            return None

        if not all_objs_email:
            return None

        for user in all_objs_email:
            if user.is_valid_password(user_pwd):
                return user

    def current_user(self, request=None) -> TypeVar('User'):
        """THis method overloads the current_user method
        """
        header = self.authorization_header(request)
        extract_64 = self.extract_base64_authorization_header(header)
        email_pwd_str = self.decode_base64_authorization_header(extract_64)
        email_pwd = self.extract_user_credentials(email_pwd_str)
        return self.user_object_from_credentials(email_pwd[0], email_pwd[1])

