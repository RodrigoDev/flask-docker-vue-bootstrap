from flask import Blueprint
from flask_restplus import Api, Resource
from .books import api as books_api
from .vehicles import api as vehicles_api
from .brands import api as brands_api

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint,
    title='Books Api',
    version='1.0',
    description='A simple book Api',
    # All API metadatas
)

api.add_namespace(books_api)
api.add_namespace(vehicles_api)
api.add_namespace(brands_api)