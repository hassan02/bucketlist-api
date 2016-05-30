import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'tests/bucketlist_test.sqlite')
SECRET_KEY = 'secret'