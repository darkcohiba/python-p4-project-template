#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource, Api

# Local imports
from config import app, api

# Add your model imports
from models import User,Trip, Signup

api = Api(app)
# Views go here!

class Index(Resource):
    def get(self):
        return make_response('<h1>Phase 4 Project Server</h1>', 200)
api.add_resource(Index, '/')

class Users(Resource):
    def get(self):
        users = [u.to_dict() for u in User.query.all()]
        return users, 200
api.add_resource(Users, '/users')

class Trips(Resource):
    def get(self):
        trips = [t.to_dict() for t in Trip.query.all()]
        return trips, 200
api.add_resource(Trips, '/trips')

class Signups(Resource):
    def get(self):
        signups = [s.to_dict() for s in Signup.query.all()]
        return signups, 200
api.add_resource(Signups, '/signups')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

