from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_moment import Moment
from config import DevConfig


db = SQLAlchemy()
# bcrypt = Bcrypt()
migrate = Migrate()
moment = Moment()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    # bcrypt.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    from .api.v1.views import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from .web_flask import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    # from auth import create_module for flask-login init
    from .auth import create_module as auth_create_module

    auth_create_module(app)
    # main_create_module(app)

    return app
