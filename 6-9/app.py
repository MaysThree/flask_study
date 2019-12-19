from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Writer(db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='writer')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    publishing_office = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    storage_time = db.Column(db.DateTime, default=datetime.now)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))


db.create_all()


@app.route('/add')
def add():
    writer1 = Writer(name='李兴华')
    writer2 = Writer(name='Mays')
    db.session.add(writer1)
    db.session.add(writer2)
    db.session.commit()

    book1 = Book(title='flask入门-钱游-1', publishing_office='forget1', isbn='124657891', writer_id='1')
    book2 = Book(title='flask入门-钱游-2', publishing_office='forget2', isbn='124657892', writer_id='2')
    book3 = Book(title='flask入门-钱游-3', publishing_office='forget3', isbn='124657893', writer_id='1')
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()
    return '添加成功'


@app.route('/select')
def select():
    writer = Writer.query.filter(Writer.id == '1').first()
    books = writer.books
    for k in books:
        print(k)
        print(k.title)

    book = Book.query.filter(Book.id == '1').first()
    writer = book.writer
    print(writer.name)
    return '查询数据库成功！'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
