from flask import Flask, flash, render_template, url_for
from flask_wtf.csrf import CSRFProtect
from forms import BaseLogin
import config

app = Flask(__name__)
app.config.from_object(config)
CSRFProtect(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=('GET', 'POST'))
def base_login():
    form = BaseLogin()
    if form.validate_on_submit():
        flash(form.name.data + '|' + form.password.data)
        return '提交成功'
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
