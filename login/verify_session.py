#! -*-coding:utf-8-*-
from flask import Blueprint, request, session, redirect, url_for, render_template
from hashlib import md5

from datamanage import checkout

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
        # Get administrator list
        userlist =
        password = [u'']
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'validly':
            if password == '123456':
                session['username'] = username
                session['password'] = password
                return redirect(url_for('login.index'))
            else:
                # 密码错误返回错误信息，注意： render_template 传递字符串时 需要用 unicode 格式
                return render_template('new_login.html', errer=u"密码错误")
        else:
            return render_template('new_login.html', errer=u"用户名错误，请校验检查用户名输入")


# 检查session是否存在，用于修饰其他 'GET' 视图函数


@verifyblue.route('/', endpoint='index')
@checkout.checksession
def index():
    return "登录成功"
