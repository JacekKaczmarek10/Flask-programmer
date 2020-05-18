from flask import Flask
from flask_testing import TestCase

from flask-programmer import app, db

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    TESTING = True


   def app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app(self)