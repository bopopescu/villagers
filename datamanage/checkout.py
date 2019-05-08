#! -*-coding:utf-8-*-
from sqlalchemy.orm import sessionmaker

from datamanage import Base, engine

# 获取具体表对象
person = Base.classes.get('person')
# 创建会话
session = sessionmaker(bind=engine)()
# 查询结果
result = session.query(person).first()

print (result)

# 插入新数据

newperson = person()