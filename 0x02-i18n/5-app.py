#!/usr/bin/env python3
""" Flask application module """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


class Config(object):
    """ Flask app configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ Gets client's locale/region
        Checks if locale has been passed in the parameters
    """
    params = request.args
    if params and params.get("locale", None):
        return params.get("locale")
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def home():
    """ Home route """
    return render_template("3-index.html")


def get_user(id) -> Dict[str, str]:
    """ Search for user in user database based
        on request id
    """
    return (users.get(id, None))


@app.before_request
def before_request():
    """ Do this before serving the
        request
    """
    params = request.args
    if params and params.get('login_as', None):
        g.user = get_user(params.get('login_as'))
        return
    g.user = None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
''
