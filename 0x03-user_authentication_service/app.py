#!/usr/bin/env python3
"""This module contains the minimal Flask app
"""
from typing import Tuple
from flask import Flask, Response, jsonify, request
from flask import make_response, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()
auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """ GET /
    Return: a JSON payload
    """
    return jsonify({"message": "Bienvenue"})


""" Task 7 """


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /users
    Return: a JSON payload
    """
    email = request.form.get('email')  # Get email from form data
    password = request.form.get('password')  # Get password from form
    try:
        auth.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


""" Task 11 """


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> Response:
    """This route checks if the email and password provided are valid
    credentials.
    return: a JSON payload if the email and password are valid
    and a 401 status code if the email and password are not valid
    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        if auth.valid_login(email, password):
            session_id = auth.create_session(email)
            resp = make_response(jsonify(
                {"email": f"{email}", "message": "logged in"}
                ))
            resp.set_cookie("session_id", session_id)
            return resp
        abort(401)
    except Exception as e:
        abort(401)

    """ Task 14 """


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> Response:
    """This route logs out a user by destroying the session ID
    and redirecting the user to the homepage.
    """
    try:
        session_id = request.cookies.get("session_id")
        if not session_id:
            abort(403)
        obj = auth._db.find_user_by(session_id=session_id)
        if obj:
            auth.destroy_session(obj.id)
            return redirect("/")
        abort(403)
    except Exception:
        abort(403)

    """ Task 15 """


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> Tuple[str, int]:
    """This route returns the profile of the user.
    """
    try:
        session_id = request.cookies.get("session_id")
        if not session_id:
            abort(403)
        email = auth.get_user_from_session_id(session_id)
        if not email:
            abort(403)
        return jsonify({"email": f"{email}"}), 200
    except Exception:
        abort(403)


""" Task 17 """


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> Tuple[str, int]:
    """Generates a reset password token and returns it in a JSON payload.
    """
    try:
        email = request.form.get("email")
        token = auth.get_reset_password_token(email)
        if not token:
            abort(403)
        return jsonify({"email": f"{email}", "reset_token": f"{token}"}), 200
    except Exception:
        abort(403)

    """ Task 19 """

@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> Tuple[str, int]:
    """This route updates the user's password with the provided reset token
    and password.
    """
    try:
        email = request.form.get("email")
        reset_token = request.form.get("reset_token")
        new_password = request.form.get("new_password")
        if not email or not reset_token or not new_password:
            abort(403)
        auth.update_password(reset_token, new_password)
        return jsonify({"email": f"{email}", "message": "Password updated"}), 200
    except Exception as e:
        return jsonify(e), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
