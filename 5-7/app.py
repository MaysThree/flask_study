from flask import Flask, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def set_session():
    session['username'] = 'mays'
    session.permanent = True
    return 'set session success'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    return username or 'session is empty'


@app.route('/del_session')
def del_session():
    session.pop('username')
    # session.clear
    return 'delete session!'


if __name__ == '__main__':
    app.run()
