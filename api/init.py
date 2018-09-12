#!/usr/bin/python

from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from project import app

db = app.config['DATABASE']

def main():
    pass_hash = generate_password_hash("tada123", method='pbkdf2:sha256')
    try:
        db.users.insert({"_id": "tada", "password": pass_hash})
        print("User created.")
    except DuplicateKeyError:
        print("User already present in DB.")


if __name__ == '__main__':
    main()
