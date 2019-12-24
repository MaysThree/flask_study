from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    tel = db.Column(db.String(11), nullable=True)
