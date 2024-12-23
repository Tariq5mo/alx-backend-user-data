#!/usr/bin/env python3
"""
Module for API authentication management.
"""
from flask import request
from typing import TypeVar, List
import os


class Auth:
    """
    Template for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that
                                            do not require authentication.

        Returns:
            bool: False, indicating that authentication is not required.
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path.endswith('/') is False:
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request (flask.Request, optional): The Flask request object.
                                                            Defaults to None.

        Returns:
            str: None, indicating no authorization header is present.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the current user from the request.

        Args:
            request (flask.Request, optional): The Flask request object.
                                                            Defaults to None.

        Returns:
            TypeVar("User"): None, indicating no current user is present.
        """
        return None

    def session_cookie(self, request=None):
        """
        Retrieves a session cookie value from the request.

        Args:
            request (flask.Request, optional): The Flask request object.
                                                            Defaults to None.

        Returns:
            str: The value of the session cookie,
                                    or None if the cookie is not present.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            cookie_value = request.cookies.get(cookie_name)
            return cookie_value
        return None
