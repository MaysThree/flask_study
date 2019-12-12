from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def user_login(func):
    def inner(*args, **kwargs):
        print('登录操作')
        func(*args, **kwargs)
    return inner


@user_login
def news():
    print(news.__name__)


news()


@user_login
def news_list(*args):
    page = args[0]
    print(news_list.__name__)
    print('这是新闻第 %s 页!' % page)


news_list(5)


if __name__ == '__main__':
    app.run()
