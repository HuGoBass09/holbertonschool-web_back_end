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
