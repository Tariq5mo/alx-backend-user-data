#!/usr/bin/env python3
"""This module contains the login route
"""
from typing import List, Tuple
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User


@app_views.route(
    "/auth_session/login", methods=["POST"], strict_slashes=False
)
def login_route() -> Tuple[str, int]:
    """login route to authenticate a user
    """
    email: str = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400
    pwd: str = request.form.get("password")
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    user_email_li: List[User] = User.search({"email": email})
    if not user_email_li:
        return jsonify({"error": "no user found for this email"}), 404
    pwd_email_li: List[User] = [
        user_pd
        for user_pd in user_email_li
        if user_pd.is_valid_password(pwd)
    ]
    if pwd_email_li:
        from api.v1.app import auth
        import os

        cookie_name = os.getenv("SESSION_NAME")
        session_id = auth.create_session(pwd_email_li[0].id)
        response = jsonify(pwd_email_li[0].to_json())
        response.set_cookie(cookie_name, session_id)
        return response, 200
    else:
        return jsonify({"error": "wrong password"}), 401

app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def delete_session():
    """Deletes the user session / logout
    """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
