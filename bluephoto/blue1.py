#! -*- coding:utf-8 -*-
"""
    Blueprint application verification account.
        datetime 19/04/27
"""

from flask import Blueprint, render_template, request
# Import the flask-login validator
from flask_login import login_required

query = Blueprint('query', __name__, template_folder='templates')


@query.route('/')
@login_required
def f():
    return render_template('bluelogin.html', url=query.root_path)


