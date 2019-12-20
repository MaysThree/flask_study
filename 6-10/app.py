from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

book_tag = db.Table('book_tag',
                    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('shelfing.id'), primary_key=True))


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    tags = db.relationship('Shelfing', secondary=book_tag, backref=db.backref('books'))


class Shelfing(db.Model):
    __tablename__ = 'shelfing'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tag = db.Column(db.String(50), nullable=False)


# db.create_all()


@app.route('/add')
def add():
    book1 = Book(name='Java开发')
    book2 = Book(name='flask入门')
    book3 = Book(name='文艺苑')
    tag1 = Shelfing(tag='文艺')
    tag2 = Shelfing(tag='计算机')
    tag3 = Shelfing(tag='技术')

    book1.tags.append(tag2)
    book1.tags.append(tag3)
    book2.tags.append(tag3)
    book3.tags.append(tag1)
    db.session.add_all([book1, book2, book3, tag1, tag2, tag3])
    db.session.commit()

    return 'add success!'


@app.route('/select')
def select():
    book = Book.query.filter(Book.name == 'Java开发').first()
    tags = book.tags
    for tag in tags:
        print(tag.tag)

    tag = Shelfing.query.filter(Shelfing.tag == '技术').first()
    books = tag.books
    for book in books:
        print(book.name)

    return 'select success!'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
