from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from Resources.userregister import UserRegister
from Resources.item import Item, ItemList
from Resources.user import Users
from Resources.store import Store,StoreList
from Db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'rajat'
api = Api(app)


db.init_app(app)


@app.before_first_request
def create_db():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/user')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
