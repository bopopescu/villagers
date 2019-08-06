#! -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple


class Loginform(Form):
    user_id = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])

