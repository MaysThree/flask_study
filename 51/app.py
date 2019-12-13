# encoding: utf-8
from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'get request'
    else:
        return 'post request'


if __name__ == '__main__':
    app.run()
