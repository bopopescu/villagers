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

query = Blueprint('query', __name__, template_folder='templates')

# Get the concrete table object
person = Base.classes.person


# data-object convert to json-object
# 单个对象
def to_dict(self):
    model_dict = dict(self.__dict__)
    del model_dict['_sa_instance_state']
    return model_dict


# 单个对象方法2
def single_to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 多个对象
def dobule_to_dict(self):
    result = {}
    for key in self.__mapper__.c.keys():
        if getattr(self, key) is not None:
            result[key] = str(getattr(self, key))
        else:
            result[key] = getattr(self, key)
    return result


person.to_dict = to_dict  # 注意:这个跟使用flask_sqlalchemy的有区别
person.single_to_dict = single_to_dict
person.dobule_to_dict = dobule_to_dict


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
        print("查询数据：", search_data)
        da = datasession.query(person).filter_by(**search_data).all()
        for numb, val in enumerate(da, 1):
            result[numb] = val.single_to_dict()
        print(result)
        return jsonify(result)
