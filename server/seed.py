#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!


        for _ in range(15):
            u = User(
                username = fake.name(),
                email = fake.email(),
                password_hash = "123abc", 
            )
            db.session.add(u)
            db.session.commit()
        
