from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
# class Base(DeclarativeBase):
#     pass

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

ma = Marshmallow()
