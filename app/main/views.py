from flask import render_template, redirect, url_for
from . import main
from flask_login import login_required

@main.route('/')
@login_required
def index():
    return render_template('index.html')

