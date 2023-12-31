#!/usr/bin/env python3
"""basic flask app"""


from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """welcome message"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'])
def register_user():
    """user registration"""
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


@app.route('/sessions', methods=['POST'])
def login():
    """user login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """user logout"""
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """user profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        response = {"email": user.email}
        return jsonify(response), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """get reset password"""
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        response = {
            'email': email,
            'reset_token': reset_token
        }
        return jsonify(response), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """update password"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        response = {
            'email': email,
            'message': 'Password updated'
        }
        return jsonify(response), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
