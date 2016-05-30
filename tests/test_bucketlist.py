import sqlite3
import unittest
import os
import hashlib
import json

from app.models import SQLAlchemy, User, BucketList, BucketListItem
from app import app
from app.helpers import *


class TestBucketList(unittest.TestCase):

    def setUp(self):
        # Clear entry in the database
        BASEDIR = os.path.abspath(os.path.dirname(__file__))
        database_name = os.path.join(BASEDIR, 'bucketlist_test.sqlite')
        db_conn = sqlite3.connect(database_name)
        db_cursor = db_conn.cursor()
        db_cursor.execute('DELETE FROM user')
        db_cursor.execute('DELETE FROM bucket_list')
        db_cursor.execute('DELETE FROM bucket_list_item')
        db_conn.commit()
        db_conn.close()
        app.config.from_object('config_test')
        self.app = app.test_client()
        self.user_data = {'username': 'test_user', 'password': 'test_password'}

    def login(self):
        self.register_request = self.app.post(
            '/auth/register', data=self.user_data)
        self.assertEqual(self.register_request.status_code, 201)
        self.login_request = self.app.post(
            '/auth/login', data=self.user_data)
        self.assertEqual(self.login_request.status_code, 200)
        result = json.loads(self.login_request.data)
        self.token = result["token"]

    def test_manage_bucketlist_without_login(self):
        self.bucketlist_request = self.app.post(
            "/bucketlists/", data={"name": "BucketList1"})
        self.assertEqual(self.bucketlist_request.status_code, 401)

    def create_bucketlist(self):
        self.login()
        self.bucketlist_request = self.app.post("/bucketlists/",
                                   data={"name": "BucketList1"},
                                   headers={"Token": self.token})
        #result = json.loads(self.bucketlist_request.data)
        #self.assertTrue(result["message"] == "Saved" and result["name"] == "BucketList1")

    def test_post_bucketlist(self):
        self.create_bucketlist()
        bucketlist = BucketList.query.filter_by(name="BucketList1").first()
        self.assertIsNotNone(bucketlist)
        #self.bucketlist_request = self.app.post('/bucketlists/', data={"name": "BucketList1"})

    def test_get_empty_bucketlist(self):
        self.login()
        self.bucketlist_request = self.app.get("/bucketlists/",  
                       data={"name": "BucketList1"},
                                   headers={"Token": self.token})
        self.assertEqual(self.bucketlist_request.status_code, 200)
        result = json.loads(self.bucketlist_request.data)
        self.assertEqual(result["message"], "Cannot locate any bucketlist for user")

    def test_create_bucketlist_item(self):
        pass


if __name__ == '__main__':
    unittest.main()
