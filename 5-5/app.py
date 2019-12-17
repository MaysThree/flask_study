from flask import Flask, request, Response
from blue_admin import bp

app = Flask(__name__)
app.register_blueprint(bp, subdomain='admin')


class Config:
    SERVER_NAME = "test.com:5000"


app.config.from_object(Config)


@app.route('/')
def set_cookie():
    resp = Response('设置cookie')
    resp.set_cookie('username', 'mays', domain='.test.com')
    return resp


@app.route('/get_cookie')
def get_cookie():
    if request.cookies.get('username'):
        username = request.cookies.get('username')
    else:
        username = 'cookie不存在!'
    return username


@app.route('/del_cookie')
def del_cookie():
    resp = Response('删除cookie')
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    app.run()
