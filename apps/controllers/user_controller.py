# -*- coding: utf-8 -*-
from apps import app
from flask import Flask, session, request, flash, url_for, redirect, render_template, abort, g
from flask.ext.login import login_user, logout_user, current_user, login_required, LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/users/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('users/register.html')
	user = User(request.form['username'], request.form['password'], request.form['email'])
	db.session.add(user)
	db.session.commit()
	flash('User successfully registered')
	return redirect(url_for('login'))

@app.route('/users/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('users/login.html')
	username = request.form['username']
	password = request.form['password']
	remember_me = False
	if 'remember_me' in request.form:
		remember_me = True
	registered_user = User.query.filter_by(username=username, password=password).first()
	if registered_user is None:
		flash('Username or Password is invalid', 'error')
		return redirect(url_for('login'))
	login_user(registered_user, remember = remember_me)
	flash('Logged in successfully')
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/users')
@login_required
def index():
	render_template('users/index.html')