import os

import flask
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
load_dotenv()

# Sử dụng biến môi trường trong ứng dụng
app.secret_key = os.getenv("SECRET_KEY")
app.debug = os.getenv("DEBUG")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

db = SQLAlchemy(app)


def createApp():
    # Tải biến môi trường từ tệp .env

    db.init_app(app)
    # ma.init_app(app)

    # Create DB
    # with app.app_context():

    db.create_all()

    # Register Model
    # app.register_blueprint(books)
    # app.register_blueprint(students)

    print('Flask version: ' + flask.__version__)

    return app

# class Students(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#     birthday = db.Column(db.Date)
#     gender = db.Column(db.String(10))
#     class_name = db.Column(db.String(10))
#
#     # borrows = db.relationship('Borrows', backref='borrow', lazy=True)
#
#     def __init__(self, name, birthday, gender, class_name):
#         self.name = name
#         self.birthday = birthday
#         self.gender = gender
#         self.class_name = class_name
#
#     def __repr__(self):
#         return '<Students %r>' % self.name
