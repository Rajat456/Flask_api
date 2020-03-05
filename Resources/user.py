from flask_jwt import jwt_required, current_identity
from flask_restful import Resource


class Users(Resource):
    @jwt_required()
    def get(self):
        user = current_identity
        print(user.username)
