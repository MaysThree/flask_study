from flask import Flask, render_template, views

app = Flask(__name__)


class Ads(views.View):
    def __init__(self):
        super().__init__()
        self.context = {'ads': '广告广告广告'}


class Index(Ads):
    def dispatch_request(self):
        return render_template('index.html', **self.context)


class Register(Ads):
    def dispatch_request(self):
        return render_template('register.html', **self.context)


class Login(Ads):
    def dispatch_request(self):
        return render_template('login.html', **self.context)


app.add_url_rule(rule='/', endpoint='index', view_func=Index.as_view('index'))
app.add_url_rule(rule='/register/', endpoint='register', view_func=Register.as_view('register'))
app.add_url_rule(rule='/login/', endpoint='login', view_func=Login.as_view('login'))


if __name__ == '__main__':
    app.run()
