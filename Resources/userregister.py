from flask_restful import Resource, reqparse
import sqlite3
from Models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank!")
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank!")

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user is None:
            user = UserModel(**data)
            user.save_to_db()
            return {'Message': 'user created Successfully'}, 201
        else:
            return  {'Message': 'User Already Exists!'}

