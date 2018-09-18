from flask_restplus import Api, Resource
from .books import api as books

api = Api(
    title='Book API',
    version='1.0',
    description='A simple book demo API',
)

@api.route('/ping')
class HealthCheck(Resource):
    def get(self):
        return {'message': 'pong!'}

api.add_namespace(books)