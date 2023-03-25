#!/usr/bin/python3
"""
    User Class for Models Module
"""
from .. import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text




class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    about_me = db.Column(db.Text(400))

    #posts = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self, email, username, password):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User {} Email {}>'.format(self.username, self.email)
