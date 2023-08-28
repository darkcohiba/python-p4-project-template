#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource, Api

# Local imports
from config import app, api, db

# Add your model imports
from models import User,Trip, Signup, TripComment, CommunityComment

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

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user.to_dict(), 200
    def patch(self, id):
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        # need to work on patch funcionality
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 200
api.add_resource(UserById, '/users/<int:id>')

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

class TripComments(Resource):
    def get(self):
        comments = [c.to_dict() for c in TripComment.query.all()]
        return comments, 200
api.add_resource(TripComments, '/tripcomments')

class CommunityComments(Resource):
    def get(self):
        comments = [c.to_dict() for c in CommunityComment.query.all()]
        return comments, 200
api.add_resource(CommunityComments, '/communitycomments')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

