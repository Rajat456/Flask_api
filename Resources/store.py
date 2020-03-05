from flask_restful import Resource, reqparse
from Models.store import StoreModel


class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name')

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'Message': 'Store Does not exist'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'Message': 'Store Already exists'}

        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json()
        except:
            return {'Message': 'Something went wrong while saving '}

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'Message': 'Store Deleted'}
        return {'Message': 'Store Does Not Exists'}


class StoreList(Resource):
    def get(self):
        return {'Store': [store.json() for store in StoreModel.query.all()]}
