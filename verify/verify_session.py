#! -*-coding:utf-8-*-
from functools import wraps
from flask import Blueprint, request, session, redirect, url_for, render_template
from flask import Markup

verifyblue = Blueprint('verify', __name__, template_folder='templates', static_folder='static')


@verifyblue.route('/new_login/', endpoint='new_login', methods=['GET', 'POST'])
def new_login():
    if request.method == 'GET':
        return render_template('new_login.html', login=url_for('verify.new_login'))
    else:
        print request.form
        userlist = [u'validly', u'zkz', u'xiaoming']
        password = [u'']
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'validly':
            if password == '123456':
                session['username'] = username
                session['password'] = password
                return redirect(url_for('verify.index'))
            else:
                # 密码错误返回错误信息，注意： render_template 传递字符串时 需要用 unicode 格式
                return render_template('new_login.html', errer=u"密码错误")
        else:
            return render_template('new_login.html', errer=u"用户名错误，请校验检查用户名输入")


# 检查session是否存在，用于修饰其他 'GET' 视图函数
def checksession(func):
    # wraps 保持函数属性
    @wraps(func)
    def verify(*args, **kwargs):
        if session.get('username') == 'validly':
            print session.get('password')
            return func(*args, **kwargs)
        else:
            return redirect(url_for('verify.new_login'))

    return verify


@verifyblue.route('/', endpoint='index')
@checksession
def index():
    return "登录成功"
