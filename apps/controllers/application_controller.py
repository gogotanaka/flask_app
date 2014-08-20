# coding: utf-8
from apps import app
from flask import Flask, session, request, flash, url_for, redirect, render_template, abort, g
from flask.ext.login import login_user, logout_user, current_user, login_required, LoginManager

@app.before_request
def before_request():
    g.user = current_user