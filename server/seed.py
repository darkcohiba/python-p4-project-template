#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        def create_users():
            users = []
            for _ in range(15):
                u = User(
                    username = fake.name(),
                    email = fake.email(),
                    password_hash = "123", 
                )
                users.append(u)
            return users
