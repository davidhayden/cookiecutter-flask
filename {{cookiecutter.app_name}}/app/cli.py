import click
from app import db
from app.auth.models import User


def register(app):
    @app.cli.command()
    def db_init():
        db.create_all()
