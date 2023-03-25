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
    role = db.Column(db.String(30), unique=True)
    role_desc = db.Column(db.String(100))

    def __init__(self, role, role_desc):
        self.role = role
        self.role_desc= role_desc

    def __repr__(self):
        return "< Role {}: Description {}>".format(self.role, self.role_desc)
        

