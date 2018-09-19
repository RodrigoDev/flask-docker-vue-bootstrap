from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'put_your_secret_key_here'

DB_NAME = 'tada'

#DATABASE = MongoClient("mongodb://localhost:27017")[DB_NAME]
DATABASE = MongoClient("mongodb://mongodb:27017")[DB_NAME]

DEBUG = True
