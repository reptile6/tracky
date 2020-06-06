from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    type = db.Column(db.String(100))
    description = db.Column(db.String(100))
    status = db.Column(db.String(100))

    def __repr__(self):
        return '<Task {}>'.format(self.description)
