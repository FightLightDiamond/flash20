import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, get_debug_queries

import flask_whooshalchemy as wa

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG'] = True
FLASKY_SLOW_DB_QUERY_TIME = 0.5
db = SQLAlchemy(app)


@app.get('/')
def index():
    return "HELLO "


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))

    def __repr__(self):
        return f'<Course: {self.name}>'


