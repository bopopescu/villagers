#! -*-coding:utf-8-*-

from datamanage import Base, datasession

# Get the concrete table object
administrator = Base.classes.administrator

def query_user(user_id):
    adminlist = datasession.query(administrator).all()
    for user in adminlist:
        if user_id == user.name:
            return user



