#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
import os
from typing import Tuple, Dict


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None


auth = os.getenv("AUTH_TYPE")
if auth == "auth":
    from api.v1.auth.auth import Auth

    auth = Auth()
elif auth == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()
elif auth == "session_auth":
    from api.v1.auth.session_auth import SessionAuth

    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_request(error) -> Tuple[Dict[str, str], int]:
    """Unauthorization handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def Forbidden_handler(error):
    """Forbidden_handler"""
    return jsonify({"error": "Forbidden"}), 403


def filter_each_request():
    """This function will be called before each request"""
    if auth is not None:
        if (
            auth.require_auth(
                request.path,
                [
                    "/api/v1/status/",
                    "/api/v1/unauthorized/",
                    "/api/v1/forbidden/",
                    "/api/v1/auth_session/login/",
                ],
            )
            is True
        ):
            if (
                auth.authorization_header(request) is None
                and auth.session_cookie(request) is None
            ):
                abort(401)
            if auth.current_user(request) is None:
                abort(403)
            request.current_user = auth.current_user(request)


app.before_request(f=filter_each_request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
