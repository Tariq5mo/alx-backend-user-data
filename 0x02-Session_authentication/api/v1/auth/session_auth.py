#!/usr/bin/env python3
"""
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """

    Args:
        Auth (_type_): _description_
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if isinstance(session_id, str):
            return SessionAuth.user_id_by_session_id.get(session_id)
        return None
