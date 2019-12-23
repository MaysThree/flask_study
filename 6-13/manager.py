from flask_script import Manager
from app import app

manager = Manager(app)


@manager.option('-n', '--name', dest='name', help='Your name', default='world')
@manager.option('-u', '--url', dest='url', default='www.csdn.com')
def hello(name, url):
    # 输入python manager.py hello --help,会显示这一行
    """hello world or hello <setting name>"""
    print('hello', name)
    print(url)


if __name__ == '__main__':
    manager.run()
