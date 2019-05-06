#! -*- coding:utf-8 -*-
"""
    Blueprint application verification account.
        datetime 19/04/27
"""

from flask import Blueprint, render_template, request
# 引入session 验证修饰接口视图函数
from verify.verify_session import checksession

query = Blueprint('query', __name__, template_folder='templates')


@query.route('/')
@checksession
def f():
    pass
    querylist = request.form
    return render_template('bluelogin.html', url=query.root_path)


