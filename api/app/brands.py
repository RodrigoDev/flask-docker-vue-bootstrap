from flask_restplus import Namespace, Resource, fields
from config import DATABASE as db
from bson.objectid import ObjectId

import json

api = Namespace('brands', description='brands operations')

class Stringfy():
    def apply(value):
        return str(value)

brand = api.model('Brands', {
    '_id': fields.Raw(readonly=True, mask=Stringfy, description='The vehicle unique identifier'),
    'name': fields.String(required=True, description='The vehicle name'),
    'description': fields.String(required=True, description='The vehicle description'),
    'is_active': fields.Boolean(required=False, description='Is an active vehicle'),
})

@api.route("/")
class BrandsList(Resource):
    @api.doc("list_brand")
    @api.marshal_list_with(brand)
    def get(self):
        '''list brands'''
        return [brand for brand in db.brand.find({})]

    @api.doc("create_brand")
    @api.expect(brand)
    @api.marshal_with(brand)
    def post(self):
        '''adding a new brand'''
        return db.brand.insert_one(api.payload), 201

@api.route("/<id>")
@api.response(404, "Brand not found")
@api.param("id", "The brand identifier")
class Brand(Resource):
    '''show a  brand'''
    @api.doc("get_brand")
    @api.marshal_with(brand)
    def get(Resource, id):
        return db.brand.find_one({
            "_id": ObjectId(id)
        })

    @api.expect(brand)
    @api.marshal_with(brand)
    def put(Resource, id):
        '''update a brand gives a identifier'''
        return db.brand.update(
            { "_id": ObjectId(id) },
            api.payload
        )

    @api.doc("delete_brand")
    @api.response(204, "Deleted branch")
    def delete(Resource, id):
        '''Delete a branch'''
        return db.brand.delete({
            "_id": ObjectId(id)
        })
