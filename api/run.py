#!/usr/bin/python
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
#cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Ping(Resource):
    def get(self):
        return {'message': 'pong'}

api.add_resource(Ping, '/ping')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)