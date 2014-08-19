# -*- coding: utf-8 -*-
from apps import app
from flask import render_template, request

@app.route('/')
def start():
	return render_template('prototype/index.html')