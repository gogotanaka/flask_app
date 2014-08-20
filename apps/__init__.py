__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////db/pakopako.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

(u'sample', u'password', u'sample@example.com', '2014-08-20 20:54:14.820484')


app.config['SECRET_KEY'] = 'random'
app.debug = True
toolbar = DebugToolbarExtension(app)
from apps.controllers import *