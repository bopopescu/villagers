#! -*- coding:utf-8 -*-
"""
    Blueprint application verification account.
        datetime 19/04/27
"""

from flask import Blueprint, render_template, request
from flask import jsonify
# Import the flask-login validator
from flask_login import login_required
from datamanage import Base, datasession

# Get the concrete table object
person = Base.classes.person

query = Blueprint('query', __name__, template_folder='templates')


@query.route('/')
@login_required
def index():
    return render_template('includes/query.html')


@query.route('/search', endpoint="query", methods=['GET', 'POST'])
@login_required
def search():
    search_data = {}
    result = {}
    if (request.method == "GET"):
        for key, value in request.args.items():
            if request.args.get(key):
                search_data[key] = value
        print("查询数据：",search_data)
        da = datasession.query(person).filter_by(**search_data).all()
        for x in da:
            print(x.name)
        return jsonify(**result)
