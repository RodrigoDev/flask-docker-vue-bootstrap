from flask_restplus import Api

from .books import api as books
#from .health_check import api as health_check

api = Api(
    title='Book API',
    version='1.0',
    description='A simple book demo API',
)

api.add_namespace(books)
#api.add_namespace(health_check)