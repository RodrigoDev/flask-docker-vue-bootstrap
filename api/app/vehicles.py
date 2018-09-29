from flask_restplus import Namespace, Resource, fields
from config import DATABASE as db
from bson.objectid import ObjectId

import json

api = Namespace('vehicles', description='vehicles operations')

class Stringfy():
    def apply(value):
        return str(value)

vehicle = api.model('Vehicle', {
    '_id': fields.Raw(readonly=True, mask=Stringfy, description='The vehicle unique identifier'),
    'name': fields.String(required=True, description='The vehicle name'),
    'description': fields.String(required=True, description='The vehicle description'),
    'is_active': fields.Boolean(required=False, description='Is an active vehicle'),
})


@api.route('/')
class VehicleList(Resource):
    @api.doc('get_vehicle')
    @api.marshal_list_with(vehicle)
    def get(self):
        '''List all books'''
        return [vehicle for vehicle in db.vehicle.find({})]

    @api.doc("create_vehicle")
    @api.expect(vehicle)
    @api.marshal_with(vehicle, code=201)
    def post(self):
        '''adding a new vehicle information'''
        return db.vehicle.insert_one(api.payload), 201

