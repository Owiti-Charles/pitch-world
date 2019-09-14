from flask import render_template,url_for,redirect
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import RegForm
from ..models import User
from .. import db

@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/signup',methods = ['POST','GET'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',r_form = form)

# @auth.route('/signup', methods = ["GET","POST"])
# def signup():
#     form = RegForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data, password = form.password.data)
#         user.save()
#         return redirect(url_for('auth.login'))
#     return render_template('auth/signup.html', r_form = form)