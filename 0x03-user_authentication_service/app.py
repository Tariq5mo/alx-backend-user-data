#!/usr/bin/env python3
"""This module contains the minimal Flask app
"""
from flask import Flask, Response, jsonify, request, session
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
    session_id = request.cookies.get("session_id")
    email = auth.get_user_from_session_id(session_id=session_id)
    obj = auth._db.find_user_by(email=email)
    if obj:
        auth.destroy_session(obj.id)
        return redirect("/")
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
