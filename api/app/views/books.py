from flask_restplus import Namespace, Resource, fields
from bson.objectid import ObjectId
from app.models.book import Book
from app.utils import update_document


api = Namespace('books', description='Books operations')

class Stringfy():
    def apply(self, value):
        return str(value)

book = api.model('Book', {
    '_id': fields.String(readonly=True, description='The book unique identifier'),
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
        return [book for book in Book.objects.all()]

    @api.doc('create_book')
    @api.expect(book)
    @api.marshal_with(book, code=201)
    def post(self):
        '''Create a new book'''
        book = Book()
        update_document(book, api.payload)
        book.save()
        return book, 201

@api.route('/<id>')
@api.response(404, 'Book not found')
@api.param('id', 'The task identifier')
class Book(Resource):
    '''Show a single book item and lets you delete them'''
    @api.doc('get_book')
    @api.marshal_with(book)
    def get(self, id):
        '''Fetch a given resource'''
        return Book.objects.find_one({
            '_id': ObjectId(id),
        })

    @api.doc('delete_book')
    @api.response(204, 'Book deleted')
    def delete(self, id):
        '''Delete a book given its identifier'''
        Book.objects.remove({
            '_id': ObjectId(id)
        })
        return '', 204

    @api.expect(book)
    @api.marshal_with(book)
    def put(self, id):
        '''Update a book given its identifier'''
        return Book.objects.update(
            {
                '_id': ObjectId(id)
            },
            api.payload
        )