#! -*-coding:utf-8-*-

from functools import wraps
from datamanage import Base,datasession
from flask import redirect, session, url_for

# Get the concrete table object
administrator = Base.classes.administrator



def checksession(func):
    # wraps :Maintains the properties of the modified function
    @wraps(func)
    def verify(*args, **kwargs):
        userimport = session.get('username')
        passwordhash = session.get('password')
        if session.get('username') == 'validly':
            print session.get('password')
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login.new_login'))

    return verify
