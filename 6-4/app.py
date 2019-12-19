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
# book1 = Book(id='001', title='flask入门-钱游', publishing_office='forget', isbn='12465789')
# try:
#     db.session.add(book1)
#     db.session.commit()
# except Exception as e:
#     print("eeerro")
#     print(e)


@app.route('/add')
def add_book():
    book1 = Book(title='flask入门-钱游-1', publishing_office='forget1', isbn='124657891')
    book2 = Book(title='flask入门-钱游-2', publishing_office='forget2', isbn='124657892')
    book3 = Book(title='flask入门-钱游-3', publishing_office='forget3', isbn='124657893')
    try:
        db.session.add(book1)
        db.session.add(book2)
        db.session.add(book3)
        db.session.commit()
        return '添加成功'
    except Exception as e:
        print(e)
        return '添加失败'


@app.route('/select')
def select():
    result = Book.query.filter(Book.publishing_office == 'forget1').all()
    print(result)
    for books in result:
        print(books.title)
    return 'query success!'


@app.route('/edit')
def edit():
    result = Book.query.filter(Book.id == '1').first()
    print(result)
    result.publishing_office = 'forget again'
    db.session.commit()
    return 'edit success!'


@app.route('/delete')
def delete():
    result = Book.query.filter(Book.id == '10').first()
    db.session.delete(result)
    db.session.commit()
    return 'delete success!'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
