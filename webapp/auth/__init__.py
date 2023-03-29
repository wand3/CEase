import functools
from flask import flash, redirect, url_for, session, abort, Blueprint
from flask_login import current_user
from flask_login import LoginManager, login_user
from flask_login import AnonymousUserMixin


auth = Blueprint('auth', __name__)
from .views import change_email, edit_profile, register, login, reset_password


class CEaseAnonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"
login_manager.anonymous_user = CEaseAnonymous


def create_module(app, **kwargs):
    login_manager.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')


def has_role(name):
    def real_decorator(f):
        def wraps(*args, **kwargs):
            if current_user.has_role(name):
                return f(*args, **kwargs)
            else:
                abort(403)
        return functools.update_wrapper(wraps, f)
    return real_decorator


@login_manager.user_loader
def load_user(userid):
    from ..models.user import User
    return User.objects.get(id=userid)
