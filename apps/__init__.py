__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
app.config['SQLALCHEMY_ECHO'] = True


app.config['SECRET_KEY'] = 'random'
app.debug = True
toolbar = DebugToolbarExtension(app)
from apps.controllers import *
