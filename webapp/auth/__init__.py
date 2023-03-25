from flask import Blueprint

auth = Blueprint('auth', __name__)
from .views import change_email, edit_profile, register, login, reset_password