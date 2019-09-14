from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required
from ..models import User
from .form import UpdateProfile
from .. import db

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)