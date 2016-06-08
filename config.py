import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'secret'

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'bucketlist.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'bucketlist-database.sqlite')

class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'tests/bucketlist_test.sqlite')
    