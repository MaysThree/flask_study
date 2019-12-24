from flask import Flask
from external import db
from models import User
import external
app = Flask(__name__)
app.config.from_object(external)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
