#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
import random
import datetime

# Local imports
from app import app
from models import db, User, Trip, Signup

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        print("deleting data")
        # db.session.delete(User.query.all())
        # db.session.delete(Trip.query.all())
        # db.session.delete(Signup.query.all())
        # db.session.commit()

        print("seeding users")
        users = []
        for _ in range(10):
            user = User(
                username = fake.user_name(),
                age = randint(18, 65),
                location = fake.city(),
                distance_traveled = randint(10, 1000),
                personal_bio = fake.text(max_nb_chars=20),
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
                description = fake.text(max_nb_chars=20),
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

        print("seeding complete")