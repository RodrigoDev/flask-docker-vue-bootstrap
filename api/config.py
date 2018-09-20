from pymongo import MongoClient
import os, pprint


env = os.environ.get('FLASK_ENV', 'local')
mongo_uri = "mongodb://{}:27017".format("mongodb" if env == "dev" else "localhost")

WTF_CSRF_ENABLED = True
SECRET_KEY = 'put_your_secret_key_here'

DB_NAME = 'tada'

#DATABASE = MongoClient("mongodb://localhost:27017")[DB_NAME]
DATABASE = MongoClient(mongo_uri)[DB_NAME]

DEBUG = True
