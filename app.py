#! -*-coding:utf-8-*-
from flask import Flask
from flask import render_template
from flask import url_for, request, redirect, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'fagpou1318#215pou'

@app.route('/web/')
@app.route('/about')
def about():
    return 'The about page,and{}'.format(app.url_map)


# 关联蓝图blue1
from bluephoto.blue1 import query
app.register_blueprint(query, url_prefix='/query')
# 关联验证登录蓝图 verifyblue
from verify.verify_session import verifyblue
app.register_blueprint(verifyblue,url_prefix='/login')

@app.route('/hello/')
@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name=None):
    if request.method == 'POST':
        # check if the request port have the file part
        if 'send' not in request.files:
            flash('no send part')
            return redirect(request.url)
        # if user not select file browser also
        # submit an empty part without filename
        fn = request.files['send']
        if fn.filename == '':
            flash('no selected file')
            return redirect(request.url)
        fn.save('C:/Users/FOX_zhao/PycharmProjects/untitled1/static/' + secure_filename(fn.filename))

    return render_template('login.html', name=name)


with app.test_request_context():
    print ('-' * 20)
    print app.url_map
    print ('-' * 20)

if __name__ == '__main__':
    app.run()
