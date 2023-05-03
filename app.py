from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'
mongo = PyMongo(app)
api = Api(app)

# Create the database if it doesn't exist
if 'users' not in mongo.db.list_collection_names():
    mongo.db.create_collection('users')

# User resource
class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = mongo.db.users.find_one({"_id": user_id})
            if user:
                return {'id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']}
            return {"message": "User not found"}, 404
        else:
            users = mongo.db.users.find()
            user_list = [{'id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']} for user in users]
            return user_list

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        user = {
            '_id': args['id'],
            'name': args['name'],
            'email': args['email'],
            'password': args['password']
        }
        mongo.db.users.insert_one(user)
        return {'id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']}, 201

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        user = mongo.db.users.find_one({"_id": user_id})
        if user:
            update_data = {}
            if args['name']:
                update_data['name'] = args['name']
            if args['email']:
                update_data['email'] = args['email']
            if args['password']:
                update_data['password'] = args['password']
            mongo.db.users.update_one({"_id": user_id}, {"$set": update_data})
            updated_user = mongo.db.users.find_one({"_id": user_id})
            return {'id': str(updated_user['_id']), 'name': updated_user['name'], 'email': updated_user['email'], 'password': updated_user['password']}
        return {"message": "User not found"}, 404

    def delete(self, user_id):
        result = mongo.db.users.delete_one({"_id": user_id})
        if result.deleted_count > 0:
            return {"message": "User deleted"}, 204
        return {"message": "User not found"}, 404

# Assign the UserResource to the desired URL endpoint
api.add_resource(UserResource, '/users', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
