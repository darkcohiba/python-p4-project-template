#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
import random
import datetime

# Local imports
from app import app
from models import db, User, Trip, Signup, TripComment, CommunityComment

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        print("deleting data")
        db.drop_all()
        db.create_all()
        # db.session.delete(User.query.all())
        # db.session.delete(Trip.query.all())
        # db.session.delete(Signup.query.all())
        # db.session.delete(TripComment.query.all())
        # db.session.delete(CommunityComment.query.all())
        db.session.commit()

        print("seeding users")
        users = []
        for _ in range(10):
            user = User(
                username = fake.user_name(),
                age = randint(18, 65),
                location = fake.city(),
                distance_traveled = random.uniform(10, 1000),
                personal_bio = fake.text(max_nb_chars=100),
            )
            user.password_hash = fake.password()
            db.session.add(user)
            db.session.commit()
            users.append(user)
        
        print("seeding trips")
        trips = []
        for _ in range(30):
            tStart = fake.date_time()
            tEnd = tStart + datetime.timedelta(hours=randint(1, 12))
            trip = Trip(
                name = fake.name(),
                owner_id = random.choice(users).id,
                description = fake.text(max_nb_chars=100),
                location = fake.city(),
                distance = randint(10, 100),
                time_start = tStart,
                time_end = tEnd,
            )
            db.session.add(trip)
            db.session.commit()
            trips.append(trip)

        print("seeding signup")
        signups = []
        for _ in range(30):
            signup = Signup(
                user_id = random.choice(users).id,
                trip_id = random.choice(trips).id,
            )
            db.session.add(signup)
            db.session.commit()
            signups.append(signup)

        print("seeding trip comments")
        trip_comments = []
        for _ in range(30):
            trip_comments = TripComment(
                content = fake.text(max_nb_chars=100),
                user_id = random.choice(users).id,
                trip_id = random.choice(trips).id,
            )
            db.session.add(trip_comments)
            db.session.commit()
            signups.append(trip_comments)

        print("seeding community comments")
        community_comments = []
        for _ in range(30):
            community_comment = CommunityComment(
                content = fake.text(max_nb_chars=100),
                user_id = random.choice(users).id,
            )
            db.session.add(community_comment)
            db.session.commit()
            signups.append(community_comment)

        print("seeding complete")

