import hashlib
import json
import os
import sqlite3
import unittest

from app.models import User, BucketList, BucketListItem
from app.app import app
from app.helpers import *
from helpers import *


class TestBucketList(unittest.TestCase):

    def setUp(self):
        setupDatabase()
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()
        self.user_data = {'username': 'test_user', 'password': 'test_password'}

    def login(self):
        self.register_response = self.app.post(
            '/api/v1/auth/register', data=self.user_data)
        self.assertEqual(self.register_response.status_code, 201)
        self.login_response = self.app.post(
            '/api/v1/auth/login', data=self.user_data)
        self.assertEqual(self.login_response.status_code, 200)
        result = json.loads(self.login_response.data)
        self.token = result['token']

    def test_manage_bucketlist_without_login(self):
        self.bucketlist_response = self.app.post(
            '/api/v1/bucketlists/', data={'name': 'BucketList1'})
        self.assertEqual(self.bucketlist_response.status_code, 401)

    def create_bucketlist_item(self):
        self.create_bucketlist()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        self.bucketlist_item_response = self.app.post('/api/v1/bucketlists/{}/items/'.format(bucketlist_id),
                                                     data={
                                                         'name': 'I want to buy a Ferrarri'},
                                                     headers={'Token': self.token})
        self.bucketlist_item = BucketListItem.query.filter_by(
            name='I want to buy a Ferrarri').first()


    def create_bucketlist(self):
        self.login()
        self.app.post('/api/v1/bucketlists/',
                      data={'name': 'BucketList1'},
                      headers={'Token': self.token})

    def test_post_bucketlist(self):
        self.create_bucketlist()
        bucketlist = BucketList.query.filter_by(name='BucketList1').first()
        self.assertIsNotNone(bucketlist)

    def test_post_bucketlist_with_existing_name(self):
        self.create_bucketlist()
        self.bucketlist_response = self.app.post('/api/v1/bucketlists/',
                                               data={'name': 'BucketList1'},
                                               headers={'Token': self.token})
        self.assertEqual(self.bucketlist_response.status_code, 400)
        result = json.loads(self.bucketlist_response.data)
        self.assertEqual(result['message'],
                         'Bucketlist already exist')

    def test_post_bucketlist_with_no_name(self):
        self.create_bucketlist()
        self.bucketlist_response = self.app.post('/api/v1/bucketlists/',
                                               data={'name': ''},
                                               headers={'Token': self.token})
        self.assertEqual(self.bucketlist_response.status_code, 400)
        result = json.loads(self.bucketlist_response.data)
        self.assertEqual(result['message'],
                         'Please supply bucketlist name')



    def test_get_empty_bucketlist(self):
        self.login()
        self.bucketlist_response = self.app.get('/api/v1/bucketlists/',
                                               headers={'Token': self.token})
        self.assertEqual(self.bucketlist_response.status_code, 200)
        result = json.loads(self.bucketlist_response.data)
        self.assertEqual(result['message'],
                         'Cannot locate any bucketlist')

    def test_get_all_bucketlist(self):
        self.create_bucketlist()
        self.bucketlist_response = self.app.get('/api/v1/bucketlists/',
                                               headers={'Token': self.token})
        result = json.loads(self.bucketlist_response.data)
        self.assertNotEqual(result, {})

    def test_put_bucketlist(self):
        self.create_bucketlist()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        self.bucketlist_response = self.app.put('/api/v1/bucketlists/{}'.format(bucketlist_id),
                                               data={'name': 'BucketList2'},
                                               headers={'Token': self.token})
        self.assertEqual(self.bucketlist_response.status_code, 200)
        bucketlist1 = BucketList.query.filter_by(name='BucketList1').first()
        bucketlist2 = BucketList.query.filter_by(name='BucketList2').first()
        self.assertIsNone(bucketlist1)
        self.assertIsNotNone(bucketlist2)

    def test_put_bucketlist_with_existing_name(self):
        self.create_bucketlist()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        self.bucketlist_response = self.app.put('/api/v1/bucketlists/{}'.format(bucketlist_id),
                                               data={'name': 'BucketList1'},
                                               headers={'Token': self.token})
        self.assertEqual(self.bucketlist_response.status_code, 406)

    def test_get_single_bucketlist(self):
        self.create_bucketlist()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        self.bucketlist_response = self.app.get('/api/v1/bucketlists/{}'.format(bucketlist_id),
                                               data={'name': 'BucketList2'},
                                               headers={'Token': self.token})
        result = json.loads(self.bucketlist_response.data)
        bucketlist_info = result['data']
        self.assertEqual(bucketlist_info['name'], 'BucketList1')
        self.assertEqual(bucketlist_info['items'], [])

    def test_delete_bucketlist(self):
        self.create_bucketlist()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        bucketlist_response = self.app.delete(
            '/api/v1/bucketlists/{}'.format(bucketlist_id), headers={'Token': self.token})
        self.assertEqual(bucketlist_response.status_code, 204)
        bucketlist = BucketList.query.filter_by(id=bucketlist_id).first()
        self.assertIsNone(bucketlist)

    def test_delete_non_existing_bucketlist(self):
        self.create_bucketlist()
        bucketlist_response = self.app.delete(
            '/api/v1/bucketlists/200', headers={'Token': self.token})
        self.assertEqual(bucketlist_response.status_code, 400)
        
    def test_post_bucketlist_item(self):
        self.create_bucketlist_item()
        self.assertIsNotNone(self.bucketlist_item)

    def test_get_single_bucketlist_item(self):
        self.create_bucketlist_item()
        self.assertIsNotNone(self.bucketlist_item)
        item_id, bucketlist_id = self.bucketlist_item.id, self.bucketlist_item.bucketlist_id
        self.bucketlist_item_response = self.app.get('/api/v1/bucketlists/{}/items/{}'.format(bucketlist_id, item_id),
                                                    headers={'Token': self.token})
        self.assertIsNotNone(self.bucketlist_item_response.data)

    def test_get_empty_bucketlist_item(self):
        self.create_bucketlist()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        bucketlist_item_response = self.app.get('/api/v1/bucketlists/{}/items/'.format(bucketlist_id),
                                               headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 200)
        result = json.loads(bucketlist_item_response.data)
        self.assertEqual(result['message'],
                         'Cannot locate any bucketlist items')

    def test_get_bucketlist_item(self):
        self.create_bucketlist_item()
        bucketlist_id = BucketList.query.filter_by(
            name='BucketList1').first().id
        bucketlist_item_response = self.app.get('/api/v1/bucketlists/{}/items/'.format(bucketlist_id),
                                               headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 200)
        self.assertIsNotNone(bucketlist_item_response)

    def test_put_bucketlist_item(self):
        self.create_bucketlist_item()
        item_id, bucketlist_id = self.bucketlist_item.id, self.bucketlist_item.bucketlist_id
        bucketlist_response = self.app.put('/api/v1/bucketlists/{}/items/{}'.format(bucketlist_id, item_id),
                                          data={
                                              'name': 'I want to buy a Sport Car', 'done': True},
                                          headers={'Token': self.token})
        self.assertEqual(bucketlist_response.status_code, 200)

    def test_put_bucketlist_item_with_existing_name(self):
        self.create_bucketlist_item()
        item_id, bucketlist_id = self.bucketlist_item.id, self.bucketlist_item.bucketlist_id
        bucketlist_item_response = self.app.put('/api/v1/bucketlists/{}/items/{}'.format(bucketlist_id, item_id),
                                          data={
                                              'name': 'I want to buy a Ferrarri'},
                                          headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 400)

    def test_post_bucketlist_item_with_existing_name(self):
        self.create_bucketlist_item()
        bucketlist_id = self.bucketlist_item.bucketlist_id
        bucketlist_item_response = self.app.post('/api/v1/bucketlists/{}/items/'.format(bucketlist_id),
                                          data={
                                              'name': 'I want to buy a Ferrarri'},
                                          headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 400)
        result = json.loads(bucketlist_item_response.data)
        self.assertEqual(result['message'],
                         'Bucketlist item already exist')

    def test_post_bucketlist_item_with_no_name(self):
        self.create_bucketlist_item()
        bucketlist_id = self.bucketlist_item.bucketlist_id
        bucketlist_item_response = self.app.post('/api/v1/bucketlists/{}/items/'.format(bucketlist_id),
                                          data={
                                              'name': ''},
                                          headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 400)
        result = json.loads(bucketlist_item_response.data)
        self.assertEqual(result['message'],
                         'Please supply name for your bucketlist item')


    def test_delete_bucketlist_item(self):
        self.create_bucketlist_item()
        item_id, bucketlist_id = self.bucketlist_item.id, self.bucketlist_item.bucketlist_id
        bucketlist_item_response = self.app.delete(
            '/api/v1/bucketlists/{}/items/{}'.format(bucketlist_id, item_id), headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 204)
        bucketlist_item = BucketListItem.query.filter_by(id=bucketlist_id).first()
        self.assertIsNone(bucketlist_item)

    def test_delete_non_existing_bucketlist_item(self):
        self.create_bucketlist_item()
        bucketlist_item_response = self.app.delete(
            '/api/v1/bucketlists/{}/items/1000'.format(self.bucketlist_item.id), headers={'Token': self.token})
        self.assertEqual(bucketlist_item_response.status_code, 400)
        

if __name__ == '__main__':
    unittest.main()
