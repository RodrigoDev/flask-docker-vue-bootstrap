from mongoengine import connect
import os
import pprint


env = os.environ.get('FLASK_ENV', 'local')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'put_your_secret_key_here'

APP_NAME = 'tada_app'
DB_NAME = 'tada'

mongo_uri = "mongodb://{}:27017/{}".format("mongodb" if env == "dev" else "localhost",
                                           DB_NAME)

DATABASE = connect(APP_NAME, mongo_uri)

DEBUG = True
