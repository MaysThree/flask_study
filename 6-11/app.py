from flask_script import Command, Manager, Server
from flask import Flask
app = Flask(__name__)
manager = Manager(app)


class Hello(Command):
    def run(self):
        print('Hello World!')


manager.add_command('hello', Hello())
# 运行python app.py runserver 不能输出hello world
manager.add_command('runserver', Server())


if __name__ == '__main__':
    # 运行命令 python app.py hello
    manager.run()
