#!/usr/bin/env python3
"""
Session Authentication Module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class for managing session authentication.
    Inherits from Auth.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id.

        Args:
            user_id (str, optional): The user ID for which
                the session ID is created. Defaults to None.

        Returns:
            str: The created session ID, or None if user_id is None
                                                        or not a string.
        """
        if isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID.

        Args:
            session_id (str, optional): The session ID to retrieve
                                        the user ID for. Defaults to None.

        Returns:
            str: The user ID associated with the session ID,
                            or None if session_id is None or not a string.
        """
        if isinstance(session_id, str):
            return SessionAuth.user_id_by_session_id.get(session_id)
        return None
