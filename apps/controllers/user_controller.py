# -*- coding: utf-8 -*-
from apps import app
from flask import render_template, request

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
	return redirect(url_for('index'))