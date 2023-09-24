import os

import flask
from flask import Flask

from .books.controller import books
from .students.controller import students
from .extension import db, ma
from .model import Students

def create_db():
    if not os.path.exists('library/library.db'):
        # with app.app_context():
        db.create_all()
        print("Created DB!")
    else:
        print('Can not create db')


def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/python'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    # ma.init_app(app)
    # Create DB
    create_db()
    # Register Model
    app.register_blueprint(books)
    app.register_blueprint(students)

    print('Flask version: ' + flask.__version__)

    return app
