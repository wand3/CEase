#!/usr/bin/python3
"""
    Role Class for Models Module
"""
from .. import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text


class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    role = db.Column(db.String(30), default='User')
    

