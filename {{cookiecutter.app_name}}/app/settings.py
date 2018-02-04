import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my-super-secret-key')
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevConfig(Config):
    DEBUG = True
