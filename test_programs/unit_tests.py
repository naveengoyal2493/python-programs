import unittest

class TestEmployee(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_email(self, email):
        self.assertEqual("naveengoyal2493@gmail.com", email)
