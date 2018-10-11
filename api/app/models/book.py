from mongoengine import Document, StringField, ReferenceField, BooleanField
from .user import User


class Book(Document):
    title = StringField(max_length=120, required=True)
    author = StringField(max_length=120)
    read = BooleanField(default=False)
    owner = ReferenceField(User)

    meta = {'allow_inheritance': True}