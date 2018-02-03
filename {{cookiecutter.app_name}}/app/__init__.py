from flask import flask
from {{cookiecutter.app_name}}.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)

    return app
