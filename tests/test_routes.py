import unittest

from app.app import app


class TestErrors(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()

    def test_invalid_resource(self):
        response = self.app.get('/bucket/')
        self.assertEqual(response.status_code, 404)

    def test_valid_resource(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_unallowed_method(self):
        response = self.app.put('api/v1/bucketlists/')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
