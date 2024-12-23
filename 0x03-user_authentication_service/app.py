#!/usr/bin/env python3
"""This module contains the minimal Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
