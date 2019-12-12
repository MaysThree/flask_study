from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def user_login(func):
    def inner():
        print('登录')
        func()
    return inner


@user_login
def news():
    print('新闻详情')


news()
# show_news = user_login(news)
# show_news()
# print(show_news.__name__)


if __name__ == '__main__':
    app.run()
