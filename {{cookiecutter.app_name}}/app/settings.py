import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my-super-secret-key')


class DevConfig(Config):
    DEBUG = True
