#! -*-coding:utf-8-*-
from flask import Blueprint, request, redirect, url_for, render_template
from hashlib import md5
from flask_login import login_user, logout_user, login_required
from datamanage import checkout, USER

# Define the blueprint
verifyblue = Blueprint('login', __name__, template_folder='templates', static_folder='static')


# Define the password encryption function
def encrypt(password=None):
    # md5().update(<values>) syntax is wrong！ py version = 2.7
    newhash = md5()
    newhash.update(password)
    token = newhash.hexdigest()
    return token


@verifyblue.route('/new_login/', endpoint='new_login', methods=['GET', 'POST'])
def new_login():
    if request.method == 'GET':
        return render_template('new_login.html', login=url_for('login.new_login'))
    else:
        user_id = request.form.get('username')
        password = request.form.get('password')
        token = encrypt(password)
        user = checkout.query_user(user_id)
        if user is not None and token == user.token:
            curr_user = USER()
            curr_user.id = user_id

            # Login to the user through the flask-login Login user method
            login_user(curr_user)
            return redirect(url_for('login.index'))

        #flash('Wrong username or password!')
        # Password error returns error message. Note that the render template passes a string in unicode format
        return render_template('new_login.html', errer=u"密码错误")



# 检查session是否存在，用于修饰其他 'GET' 视图函数


@verifyblue.route('/', endpoint='index')
@login_required
def index():
    return "登录成功"

@verifyblue.route('/logout')
@login_required
def logout():
    logout_user()
    return "Logging out successfully!"
