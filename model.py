import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, get_debug_queries

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config['SQLALCHEMY_ECHO'] = True
FLASKY_SLOW_DB_QUERY_TIME = 0.5
db = SQLAlchemy(app)


user_channel = db.Table('user_channel',
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                        db.Column('channel_id', db.Integer, db.ForeignKey('channel.id')),
                        )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)
    following = db.relationship('Channel', secondary=user_channel, backref='followers')

    def __repr__(self):
        return f'<User: {self.email}>'


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    pets = db.relationship('Pet', backref='owner')


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f'<Channel: {self.name}>'

