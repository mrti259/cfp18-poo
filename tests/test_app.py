import unittest
from flaskr.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
