import os


env = os.environ.get('FLASK_ENV', 'local')

class BaseConfig():
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'put_your_secret_key_here'
    DEBUG = True

class DevConfig(BaseConfig):
    APP_NAME = 'tada_app'
    DB_NAME = 'tada'
    MONGODB_SETTINGS = {
        'db': DB_NAME,
        'host': "mongodb" if env == "dev" else "localhost",
        'port': 27017
    }