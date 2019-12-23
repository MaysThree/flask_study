from flask_script import Manager
from app import app

manager = Manager(app)


@manager.command
def hello():
    print('Hello World')


if __name__ == '__main__':
    manager.run()
