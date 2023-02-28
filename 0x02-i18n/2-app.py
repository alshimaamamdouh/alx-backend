#!/usr/bin/env python3
""" Flask application module """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """ Configuration class """
    LANGUAGES = ["en", "fr"]

# Default locale.
app.config["BABEL_DEFAULT_LOCALE"] = Config.LANGUAGES[0]


@babel.localeselector
def get_locale():
    """ Gets clients locale/region"""
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route("/", strict_slashes=False)
def home():
    """ Home route """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
