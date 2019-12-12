# encoding:utf-8
from flask import Flask, render_template, request, views

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


class LoginView(views.MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        username = request.form.get('username')
        password = request.form.get('pwd')
        if username == 'admin' and password == 'admin':
            return '登录成功'
        else:
            return '用户名或密码错误'


app.add_url_rule('/login', view_func=LoginView.as_view('lognview'))


if __name__ == '__main__':
    app.run()
