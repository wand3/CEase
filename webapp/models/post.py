#!/usr/bin/python3
"""
    Post and Tag Class for Models Module
    - many to many relationship with tags
"""
from .. import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from ..models.user import *
from ..models.post import *
import datetime
# from ..models.comment import Comment

tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class Post(db.Model):
    ___tablename__ = "post"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts', lazy='dynamic'), lazy='dynamic'
        # secondaryjoin=(tags.c.tag_id == id)
    )

    def __init__(self, title=""):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)




class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    # tag_id = db.Column(db.Integer, db.ForeignKey(''))

    def __init__(self, title):
        self.title = title
    def __repr__(self):
        return "<Tag '{}'>".format(self.title)
    

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))



    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return "< Comment {}>".format(self.text[:10])