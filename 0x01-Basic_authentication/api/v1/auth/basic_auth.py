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

        Args:
            authorization_header (str): _description_

        Returns:
            str: _description_
        """
        auth_head = authorization_header
        if isinstance(auth_head, str) and auth_head.startswith("Basic "):
            return auth_head.split(" ")[1]
        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: _description_
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

        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        email_pass = decoded_base64_authorization_header
        if isinstance(email_pass, str) and email_pass.find(":") != -1:
            return email_pass.split(":")[0], email_pass.split(":")[1]
        return None, None

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """

        Args:
            self (_type_): _description_
        """
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            all_objs_email: List[User] = User.search({"email": user_email})
            if all_objs_email == []:
                return None
            all_objs_pwd: List[User] = [
                obj
                for obj in all_objs_email
                if obj.is_valid_password(user_pwd)
            ]
            if all_objs_pwd == []:
                return None
            return all_objs_pwd[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        header = self.authorization_header(request)
        extract_64 = self.extract_base64_authorization_header(header)
        email_pwd_str = self.decode_base64_authorization_header(extract_64)
        email_pwd = self.extract_user_credentials(email_pwd_str)
        return self.user_object_from_credentials(email_pwd[0], email_pwd[1])
