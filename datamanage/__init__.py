#! -*-coding:utf-8-*-

"""
    Import sqlalchemy module control databases,easy to find and modify relate database objects.
Directly reflects existing tables in the database, providing existing table classes
"""
from flask_login import UserMixin
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

# Database dialect type
mysql = 'mysql'
# The database link driver module is mysql-connector-python
driver = 'mysqlconnector'
# User \ password \ server \ port \ database
user = 'root'
password = 'hp2548HPL'
host = 'localhost'
port = 3306
database = 'messages'

parameters = dict(
    dialect=mysql,
    driver=driver,
    user=user,
    password=password,
    host=host,
    port=port,
    database=database
)

# Get the database interface url
dataurl = "{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}".format(**parameters)

# To create a connection
# NOTE: the pool is created by default. When the mysql server is disconnected, session operation exception will be caused.Have access to sqlalchemy.pool.Nullpool.
# eg:
# engine = create_engine(dataurl,poolclass=NullPool)
engine = create_engine(dataurl)

# Building metadata
metadata = MetaData(bind=engine)

# Reflection databases
Base = automap_base()
Base.prepare(engine=engine, reflect=True)

# Create databases session
datasession = sessionmaker(bind=engine)()

# Create a simple login user classes
class USER(UserMixin):
    pass