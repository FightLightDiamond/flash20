import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DB_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
