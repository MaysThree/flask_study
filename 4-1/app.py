from flask import Flask, url_for

app = Flask(__name__)


@app.route('/', endpoint='index')
def hello_world():
    return 'Hello World!'


def my_test():
    return '测试视图函数'


app.add_url_rule('/test/', endpoint='test', view_func=my_test)
with app.test_request_context():
    print(url_for('test'))


if __name__ == '__main__':
    app.run()
