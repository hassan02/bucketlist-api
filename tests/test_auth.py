import unittest
import hashlib

from app.models import SQLAlchemy, User, BucketList, BucketListItem
from app.app import app
from app.helpers import *
from helpers import *


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        # Clear entry in the database
        setupDatabase()
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()
        self.register_user()

    def register_user(self):
        test_data = {'username': 'test_user', 'password': 'test_password'}
        self.register_response = self.app.post(
            '/api/v1/auth/register', data=test_data)

    def login_with_invalid_details(self):
        test_data = {'username': 'andela', 'password': 'andela'}
        self.login_response = self.app.post(
            '/api/v1/auth/login', data=test_data)

    def test_register_user(self):
        user = User.query.filter_by(username='test_user',
                                    password=hashlib.sha512(
                                        'test_password').hexdigest()).first()
        self.assertEqual(self.register_response.status_code, 201)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, hashlib.sha512(
            'test_password').hexdigest())

    def test_valid_user_login(self):
        self.login_response = self.app.post(
            '/api/v1/auth/login', data={'username': 'test_user',
                                        'password': 'test_password'})
        self.assertEqual(self.login_response.status_code, 200)

    def test_login_with_invalid_username(self):
        self.login_response = self.app.post(
            '/api/v1/auth/login', data={'username': 'andela',
                                        'password': 'test_password'})
        self.assertEqual(self.login_response.status_code, 406)

    def test_login_with_invalid_password(self):
        self.login_response = self.app.post(
            '/api/v1/auth/login', data={'username': 'test_user',
                                        'password': 'andela'})
        self.assertEqual(self.login_response.status_code, 406)

    def test_login_with_blank_details(self):
        self.login_response = self.app.post(
            '/api/v1/auth/login', data={'username': '',
                                        'password': 'andela'})
        self.assertEqual(self.login_response.status_code, 406)

    def test_register_with_existing_username(self):
        self.register_another_user = self.app.post(
            '/api/v1/auth/register', data={'username': 'test_user',
                                           'password': 'andela'})
        self.assertEqual(self.register_another_user.status_code, 406)

    def test_register_with_blank_details(self):
        self.register_response = self.app.post(
            '/api/v1/auth/register', data={'username': '',
                                           'password': 'andela'})
        self.assertEqual(self.register_response.status_code, 406)


if __name__ == '__main__':
    unittest.main()
