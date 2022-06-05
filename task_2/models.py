from unittest import result
from task_2 import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(), nullable=False)   

class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer(), primary_key=True)
    result = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id'), nullable=False)
    subject_id = db.Column(db.Integer(), db.ForeignKey(
        'subjects.id'), nullable=False)

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
