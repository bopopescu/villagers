#! -*-coding:utf-8-*-
from flask import Blueprint, request, redirect, url_for, render_template, session
from flask import jsonify
import json
from hashlib import md5
from flask_login import login_user, logout_user, login_required
from datamanage import checkout, USER
from login.myform import Loginform

# Define the blueprint
verifyblue = Blueprint('login', __name__, template_folder='templates', static_folder='static')


# Define the password encryption function
def encrypt(password=None):
    # md5().update(<values>) syntax is wrong！ py version = 2.7
    newhash = md5()
    newhash.update(password.encode('utf-8'))
    token = newhash.hexdigest()
    return token


@verifyblue.route('/new_login/', endpoint='new_login', methods=['GET', 'POST'])
def new_login():
    # Record the page address before authentication with the session
    oldargs = request.args.get('next')
    if oldargs:
        session['old_args_next'] = oldargs
    if request.method == 'GET':
        loginform = Loginform()
        return render_template('new_login.html', form=loginform)
    else:
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        token = encrypt(password)
        user = checkout.query_user(user_id)
        if user is not None and token == user.token:
            curr_user = USER()
            curr_user.id = user_id

            # Login to the user through the flask-login Login user method
            login_user(curr_user)
            # After successful verification,jump to the original request page.
            return redirect(session.get('old_args_next'))

        # flash('Wrong username or password!')
        # Password error returns error message. Note that the render template passes a string in unicode format
        return render_template('new_login.html', errer=u"密码错误")


# 检查session是否存在，用于修饰其他 'GET' 视图函数

@verifyblue.route('/logout')
@login_required
def logout():
    logout_user()
    return "Logging out successfully!"


# template test function
@verifyblue.app_template_test('current_link')
def is_current_link(link):
    return link == request.path
