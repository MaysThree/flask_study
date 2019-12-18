# encoding: utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
