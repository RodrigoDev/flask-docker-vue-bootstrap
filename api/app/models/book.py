from mongoengine import Document, StringField, ReferenceField, BooleanField, ObjectIdField
from .user import User
from bson.objectid import ObjectId


class Book(Document):
    _id = ObjectIdField(required=True, default=ObjectId())
    title = StringField(max_length=120, required=True)
    author = StringField(max_length=120)
    read = BooleanField(default=False)
    owner = ReferenceField(User)

    meta = {'allow_inheritance': True}