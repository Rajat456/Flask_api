from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from Models.Item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This Field Cannot be blank!")
    parser.add_argument('store_id', type=int, required=True, help="Every Item Needs a Store_id")
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item Not Found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'Message': 'Item Already Exists'}, 400

        request_data = Item.parser.parse_args()
        item = ItemModel(name, request_data['price'], request_data['store_id'])
        ItemModel.save_to_db(item)

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'Message': 'Item Deleted'}

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
