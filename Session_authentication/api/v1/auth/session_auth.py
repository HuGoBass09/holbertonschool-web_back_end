#!/usr/bin/env python3
""" Module of Session Authentication
"""

from api.v1.auth.auth import Auth
from typing import Dict, TypeVar
from models.user import User
from flask import request
import uuid


class SessionAuth(Auth):
    """Session Authentication Class inherited from Auth"""

    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID"""
        if user_id is None or type(user_id) is not str:
            return None
        session_id: str = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current_user method that returns a User instance"""
        cookie: str = self.session_cookie(request)
        user_id: str = self.user_id_for_session_id(cookie)
        user: TypeVar("User") = User.get(user_id)

        return user

    def destroy_session(self, request=None):
        """DELETE /auth_session/logout"""
        if request is None:
            return False

        session_id: str = self.session_cookie(request)

        if session_id is None:
            return False

        user_id: str = self.user_id_for_session_id(session_id)

        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]

        return True
