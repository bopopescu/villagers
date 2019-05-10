#! -*-coding:utf-8-*-
from flask import Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'fagpou1318#215pou'

# 关联蓝图blue1
from bluephoto.blue1 import query

app.register_blueprint(query, url_prefix='/query')
# 关联验证登录蓝图 login-blue
from login.verify_session import verifyblue

app.register_blueprint(verifyblue, url_prefix='/login')


# 打印应用所有的路由
with app.test_request_context():
    print ('-' * 20)
    print app.url_map
    print ('-' * 20)
# 本程序运行
if __name__ == '__main__':
    app.run()
