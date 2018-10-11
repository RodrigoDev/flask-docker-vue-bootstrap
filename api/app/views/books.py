from flask_restplus import Namespace, Resource, fields
from bson.objectid import ObjectId
from services import BookService, UserService

import json

api = Namespace('books', description='Books operations')

class Stringfy():
    def apply(self, value):
        return str(value)

book = api.model('Book', {
    '_id': fields.Raw(readonly=True, mask=Stringfy, description='The book unique identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author name'),
    'read': fields.Boolean(required=False, description='Already read the book'),
})

@api.route('/')
class BookList(Resource):
    @api.doc('list_books')
    @api.marshal_list_with(book)
    def get(self):
        '''List all books'''
        return [book for book in db.book.find({})]

    @api.doc('create_book')
    @api.expect(book)
    @api.marshal_with(book, code=201)
    def post(self):
        '''Create a new book'''
        return db.book.insert_one(api.payload), 201

@api.route('/<id>')
@api.response(404, 'Book not found')
@api.param('id', 'The task identifier')
class Book(Resource):
    '''Show a single book item and lets you delete them'''
    @api.doc('get_book')
    @api.marshal_with(book)
    def get(self, id):
        '''Fetch a given resource'''
        return db.book.find_one({
            '_id': ObjectId(id),
        })

    @api.doc('delete_book')
    @api.response(204, 'Book deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        db.book.remove({
            '_id': ObjectId(id)
        })
        return '', 204

    @api.expect(book)
    @api.marshal_with(book)
    def put(self, id):
        '''Update a task given its identifier'''
        return db.book.update(
            {
                '_id': ObjectId(id)
            },
            api.payload
        )