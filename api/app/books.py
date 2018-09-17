from flask_restplus import Namespace, Resource, fields
import uuid

api = Namespace('books', description='Books operations')

book = api.model('Book', {
    'id': fields.Integer(readonly=True, description='The book unique identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author name'),
    'read': fields.Boolean(required=False, description='Already read the book'),
})

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@api.route('/')
class BookList(Resource):
    @api.doc('list_books')
    @api.marshal_list_with(book)
    def get(self):
        '''List all books'''
        return BOOKS


@api.route('/<int:id>')
@api.response(404, 'Book not found')
@api.param('id', 'The task identifier')
class Book(Resource):
    '''Show a single book item and lets you delete them'''
    @api.doc('get_book')
    @api.marshal_with(book)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @api.doc('delete_book')
    @api.response(204, 'Book deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @api.expect(book)
    @api.marshal_with(book)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)