#!/usr/bin/env python3
"""basic flask app"""

from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name)


@app.route("/", methods=["GET"])
def welcome():
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'])
def register_user():
    try:
        email = request.form['email']
        password = request.form['password']
        if email is None or password is None:
            abort(400)

        user = AUTH.register_user(email, password)

        response = {
            'email': user.email,
            'message': 'user created'
        }
        return jsonify(response), 200
    except ValueError as e:
        response = {
            'message': 'email already registered'
        }
        return jsonify(response), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
