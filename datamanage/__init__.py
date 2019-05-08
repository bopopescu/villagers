#! -*-coding:utf-8-*-

"""
    Import sqlalchemy module control databases,easy to find and modify relate database objects.
Directly reflects existing tables in the database, providing existing table classes
"""

from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.pool import NullPool

# 数据库方言类型
mysql = 'mysql'
# 数据库链接驱动程序模块为 mysql-connector-python
driver = 'mysqlconnector'
# 用户\密码\服务器\端口\数据库
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

# 获取数据库接口url
dataurl = "{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}".format(**parameters)

# 创建连接,注意 : 默认创建pool池,当mysql服务器断开时会造成session操作异常,要么使用 sqlalchemy.pool.Nullpool ,如下
# engine = create_engine(dataurl,poolclass=NullPool)
engine = create_engine(dataurl)

# 构建元数据
metadata = MetaData(bind=engine)

# 反射数据库
Base = automap_base()
Base.prepare(engine=engine, reflect=True)




