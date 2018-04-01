from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from settings import Config


db = SQLAlchemy()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
toolbar = DebugToolbarExtension()


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    login.init_app(app)
    toolbar.init_app(app)


def register_blueprints(app):
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.dashboard import bp as dash_bp
    app.register_blueprint(dash_bp)

    from app.errors import bp as err_bp
    app.register_blueprint(err_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
