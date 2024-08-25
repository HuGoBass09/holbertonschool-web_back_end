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
