from app import app
import unittest

class TodoTestCase(unittest.TestCase):  

    def setUp(self):  
        self.app = app.test_client()  

    def tearDown(self):  
        pass  

    def test_index(self):  
        rv = self.app.get('/')  
        assert "markdown-body" in rv.data