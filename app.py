#! -*-coding:utf-8-*-
from flask import Flask
from flask_login import LoginManager

from datamanage import checkout, USER

# Create application object
app = Flask(__name__)

# Create an instance of LoginManager and bind it to the app
loginmanager = LoginManager()
loginmanager.login_view = 'login.new_login'
loginmanager.login_message_category = 'info'
loginmanager.login_message = 'ACCESS DENY!'
loginmanager.init_app(app)


#   Define user_callback function
@loginmanager.user_loader
def load_user(user_id):
    if checkout.query_user(user_id) is not None:
        curr_user = USER()
        curr_user.id = user_id

        return curr_user


app.secret_key = 'fagpou1318#215pou'

# Bind blue1 of Blueprints
from bluephoto.blue1 import query

app.register_blueprint(query, url_prefix='/query')
# Bind login-blue of Blueprints
from login.index import verifyblue

app.register_blueprint(verifyblue, url_prefix='/login')

@app.route('/')
def home():
    return '主页'
# 打印应用所有的路由
with app.test_request_context():
    print ('-' * 20)
    print app.url_map
    print ('-' * 20)
# 本程序运行
if __name__ == '__main__':
    app.run()
