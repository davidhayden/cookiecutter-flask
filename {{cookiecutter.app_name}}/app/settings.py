class Config(object):
    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'my-super-secret-key')


class DevConfig(Config):
    DEBUG = True
