from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# db.init_app(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    publishing_office = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    storage_time = db.Column(db.DateTime, default=datetime.now)


# db.create_all()
book1 = Book(id='001', title='flask入门-钱游', publishing_office='forget', isbn='12465789')
try:
    db.session.add(book1)
    db.session.commit()
except Exception as e:
    print("eeerro")
    print(e)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
