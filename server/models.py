from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import db, bcrypt



# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)
    distance_traveled = db.Column(db.Float, nullable=False)
    personal_bio = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    signups = db.relationship("Signup", cascade="all,delete-orphan", backref="users")
    trip_comments = db.relationship("TripComment", cascade="all,delete-orphan", backref="users")
    community_comments = db.relationship("CommunityComment", cascade="all, delete-orphan", backref="users")

    @validates("username")
    def validate_username(self, key, value):
        usernames = User.query.with_entities(User.username).all()
        if not value and value in usernames:
            raise ValueError("Username must be unique")
        return value

    @validates("personal_bio")
    def validate_personal_bio(self, key, value):
        if len(value) < 0 and len(value) > 500:
            raise ValueError("Persoal bio must be between 0 and 500 characters")
        return value

    @validates("age")
    def validate_age(self, key, value):
        if value < 0 and value > 100:
            raise ValueError("Age must be between 0 and 100")
        return value

    serialize_rules = ("-signups.users", "-trip_comments.users", "-community_comments.users",)
    @hybrid_property
    def password_hash(self):
        raise Exception("Password hashes may not be viewed")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    @validates("username")
    def validate_username(self, key, value):
        usernames = User.query.with_entities(User.username).all()
        if not value and value in usernames:
            raise ValueError("Username must be unique")
        return value


class Trip(db.Model, SerializerMixin):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    location = db.Column(db.String, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    signups = db.relationship("Signup", cascade="all, delete-orphan", backref="trips")
    trip_comments = db.relationship("TripComment", cascade="all, delete-orphan", backref="trips")

    @validates("description")
    def validate_description(self, key, value):
        if len(value) < 0 and len(value) > 1500:
            raise ValueError("Description must be between 0 and 1500 characters")
        return value

    serialize_rules = ("-signups.trips","-trip_comments.trips",)

class Signup(db.Model, SerializerMixin):
    __tablename__ = 'signups'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ("-users.signups", "-trips.signups","-users.trip_comments", "-trips.trip_comments",)

class TripComment(db.Model, SerializerMixin):
    __tablename__ = 'trip_comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("content")
    def validate_content(self, key, value):
        if len(value) < 0 and len(value) > 500:
            raise ValueError("Content must be between 0 and 500 characters")
        return value

    serialize_rules = ("-users.trip_comments", "-trips.trip_comments","-users.signups", "-trips.signups",)

class CommunityComment(db.Model, SerializerMixin):
    __tablename__ = 'community_comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates("content")
    def validate_content(self, key, value):
        if len(value) < 0 and len(value) > 500:
            raise ValueError("Content must be between 0 and 500 characters")
        return value

    serialize_rules = ("-users.community_comments",)