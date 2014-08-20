# coding: utf-8

class User(db.Model):
	__tablename__ = "users"
	id = db.Column('user_id',db.Integer , primary_key=True)
	username = db.Column('username', db.String(20), unique=True , index=True)
	password = db.Column('password' , db.String(10))
	email = db.Column('email',db.String(50),unique=True , index=True)
	created_at = db.Column('created_at' , db.DateTime)

	def __init__(self , username ,password , email):
		self.username = username
		self.password = password
		self.email = email
		self.created_at = datetime.utcnow()

	def is_autherized(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)

from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.init_appapp()

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))