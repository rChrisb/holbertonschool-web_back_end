#!/usr/bin/env python3
"""basic flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user(user_id=None):
    """get a user"""
    if user_id is not None:
        user = users.get(user_id)
    else:
        user = g.user

    return user


@app.before_request
def before_request():
    """user info"""
    user_id = request.args.get("login_as")
    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """get locale from request"""
    locale = request.args.get('locale')
    if g.user and "locale" in g.user and g.user["locale"] in
    app.config["LANGUAGES"]:
        locale = g.user["locale"]
    if not locale:
        header_locale = request.accept_languages.best_match(
            app.config["LANGUAGES"])
        if header_locale in app.config["LANGUAGES"]:
            locale = header_locale
    if not locale:
        locale = app.config["BABEL_DEFAULT_LOCALE"]
    return locale


@app.route('/')
def index():
    """rendering template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
