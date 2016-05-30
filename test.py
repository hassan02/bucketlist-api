import unittest

tests = unittest.TestLoader().discover('tests')
unittest.TextTestRunner().run(tests)