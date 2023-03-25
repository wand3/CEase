import os
from dotenv import load_dotenv
import create_db


class Config(object):
    SECRET_KEY = 'chequestillunsigned'


class DevConfig(Config):
    DEBUG = True
    #sqlite db uri
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

    #mysql db uri
    SQLALCHEMY_DATABASE_URI = 'mysql://root:cease@localhost/cease_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
