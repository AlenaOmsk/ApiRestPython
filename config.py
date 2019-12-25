import os
basedir = os.path.abspath(os.path.dirname(__file__))
import psycopg2

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    #db_url = "postgresql://Salem:1qazxsw23edc@localhost:5432/python_res" 
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:12345@localhost:5432/results"
class ProductionConfig(Config):
    DEBUG = False
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
