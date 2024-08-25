#!/usr/bin/env python3
"""app module"""

from flask import Flask, abort, jsonify, request, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def index():
    """GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> str:
    """A method to create a new user"""
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)

    except ValueError:
        message = {"message": "email already registered"}
        return jsonify(message), 400

    message = {"email": user.email, "message": "user created"}

    return jsonify(message)


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """login function"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": "{}".format(email),
                            "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)
