import unittest

from app import app

class TestErrors(unittest.TestCase):
	"""Test Cases for Errors"""
	def setUp(self):
		app.config.from_object('config_test')
		self.app = app.test_client()

	def test_invalid_resource(self):
		response = self.app.get('/bucket/')
		self.assertEqual(response.status_code, 404)

	def test_valid_resource(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

	def test_unallowed_method(self):
		response = self.app.put('/bucketlists/')
		self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
