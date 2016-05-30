import sqlite3
import unittest
import os
import hashlib

from app.models import SQLAlchemy, User, BucketList, BucketListItem
from app import app
from app.helpers import *


class TestBucketList(unittest.TestCase):

    def setUp(self):
        # Clear entry in the database
        BASEDIR = os.path.abspath(os.path.dirname(__file__))
        database_name = os.path.join(BASEDIR, 'test_bucketlist.sqlite')
        db_conn = sqlite3.connect(database_name)
        db_cursor = db_conn.cursor()
        db_cursor.execute('DELETE FROM user')
        db_cursor.execute('DELETE FROM bucket_list')
        db_cursor.execute('DELETE FROM bucket_list_item')
        db_conn.commit()
        db_conn.close()
        app.config.from_object('config_test')
        self.app = app.test_client()

    def register_user(self):
        test_data = {'username': 'test_user', 'password': 'test_password'}
        self.register_request = self.app.post('/auth/register', data=test_data)

    def login_with_invalid_details(self):
        self.register_user()
        test_data = {'username': 'andela', 'password': 'andela'}
        self.login_request = self.app.post('/auth/login', data=test_data)

    def test_register_user(self):
        self.register_user()
        user = User.query.filter_by(username='test_user', password=hashlib.sha512(
            'test_password').hexdigest()).first()
        self.assertEqual(self.register_request.status_code, 201)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, hashlib.sha512(
            "test_password").hexdigest())

    def test_valid_user_login(self):
        self.register_user()
        self.login_request = self.app.post(
            '/auth/login', data={'username': 'test_user', 'password': 'test_password'})
        self.assertEqual(self.login_request.status_code, 200)

    def test_login_with_invalid_username(self):
        self.register_user()
        self.login_request = self.app.post(
            '/auth/login', data={'username': 'andela', 'password': 'test_password'})
        self.assertEqual(self.login_request.status_code, 406)

    def test_login_with_invalid_password(self):
        self.register_user()
        self.login_request = self.app.post(
            '/auth/login', data={'username': 'test_user', 'password': 'andela'})
        self.assertEqual(self.login_request.status_code, 406)

    def test_login_with_blank_details(self):
        self.register_user()
        self.login_request = self.app.post(
            '/auth/login', data={'username': '', 'password': 'andela'})
        self.assertEqual(self.login_request.status_code, 406)

    def test_register_with_existing_username(self):
      self.register_user()
      self.register_another_user = self.app.post('/auth/register', data={'username': 'test_user', 'password': 'andela'})
      self.assertEqual(self.register_another_user.status_code, 406)

    def test_register_with_blank_details(self):
      self.register_request = self.app.post('/auth/register', data={'username': '', 'password': 'andela'})
      self.assertEqual(self.register_request.status_code, 406)

    



if __name__ == '__main__':
    unittest.main()
