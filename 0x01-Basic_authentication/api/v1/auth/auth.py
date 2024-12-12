#!/usr/bin/env python3
"""
Module for API authentication management.
Task 3
"""
from flask import request
from typing import TypeVar, List


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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request (flask.Request, optional): The Flask request object.
                                                            Defaults to None.

        Returns:
            str: None, indicating no authorization header is present.
        """
        return None

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
