#!/usr/bin/python3
"""
    User Class for Models Module
"""
from .. import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from ..models.roles import Roles
from ..models.post import *

roles = db.Table(
    'user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
    )

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    institution = db.Column(db.String(255))
    about_me = db.Column(db.Text(400))

    roles = db.relationship(
        'Roles',
        secondary=roles,
        backref=db.backref('user', lazy='dynamic'), lazy='dynamic'
        )

    posts = db.relationship(
        'Post', 
        backref='poster',
        lazy='dynamic'
        )
    

    def __init__(self, email, username, password, about_me, institution):
        self.username = username
        self.password = password
        self.email = email
        self.about_me = about_me
        self.institution = institution

    def __repr__(self):
        return '<User {} Email {} About me {}>'.format(self.username, self.email, self.about_me)


# db.drop_all()
# db.create_all()

# e1 = User(username='John', 
# password='3r4r34f',email='jd@example.com',
#     about_me='   cefjif about me  '
# )
# e2 = User(username='Mary', 
# password='3r4r34f',email='md@example.com',
#     about_me='   cefjif about me  ')

# e3 = User(username='Jane',
# password='3r4r34f',
#               email='jt@example.com',
#               agbout_me='2, cefjif about me '
#               )

# e4 = User(username='Alex',
# password='3r4r34f',
#               email='ab@example.com',
#               about_me='2 cefjif about me 9'
#               )

# e5 = User(username='James',
# password='3r4r34f',
#               email='jw@example.com',
#               about_me='2 cefjif about me 4'
#               )

# e6 = User(username='Harold',
# password='3r4r34f',
#               email='hi@example.com',
#               about_me='52 cefjif about me ,'
#               )

# e7 = User(username='Scarlett',
# password='3r4r34f',
#               email='sw@example.com',
#               about_me='2 cefjif about me 2'
#               )

# e8 = User(username='Emily',
# password='3r4r34f',
#               email='ev@example.com',
#               about_me='2 cefjif about me 7'
#               )

# e9 = User(username='Mary',
#               email='mp@example.com',
#               password='3r4r34f',
#               about_me='30 cefjif about me ,'
#               )

# db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8, e9])

# db.session.commit()