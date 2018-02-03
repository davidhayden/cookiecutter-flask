from flask import Flask
from flask_bootstrap import Bootstrap
from app.settings import DevConfig


bootstrap = Bootstrap()


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    bootstrap.init_app(app)


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
