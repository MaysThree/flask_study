from flask import Flask
import time

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print('before_first_request')


@app.before_request
def before_request():
    print('before_request')


@app.after_request
def after_request(response):
    print('after_request')
    response.headers['Content-Type'] = 'application/json'
    return response


@app.teardown_request
def teardown_request(e):
    print('teardown_request')


@app.route('/')
def hello_world():
    print('visit index!')
    time.sleep(5)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
