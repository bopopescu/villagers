#! -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Email


class Loginform(FlaskForm):
    user_id = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])

