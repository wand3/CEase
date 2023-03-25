from flask import Blueprint

api = Blueprint('api', __name__)
from . import activity, comments, groups, institutions,\
      messages, posts, trends, users