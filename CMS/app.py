from flask import Flask
from apps.admin import bp as admin_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
DEBUG = True
app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # TODO: 有其他安排，暂停学习
    app.run()
