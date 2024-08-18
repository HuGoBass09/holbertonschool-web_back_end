#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth method that returns
        True if the path is not in the list
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] is not "/":
            path += "/"

        for paths in excluded_paths:
            if paths.endswith("*"):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header method that returns none"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """current_user method that returns None"""
        return request
