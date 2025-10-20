import unittest
import json
from app.server.handler import APIHandler
from app.config import Config

class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        self.handler = APIHandler()
        
    def test_health_check(self):
        response = self.handler.handle_health_check()
        data = json.loads(response['body'])
        
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], Config.APP_NAME)
        self.assertEqual(data['version'], Config.VERSION)
        
    def test_not_found(self):
        response = self.handler.handle_not_found()
        data = json.loads(response['body'])
        
        self.assertEqual(response['status_code'], 404)
        self.assertEqual(data['error'], 'Not Found')

if __name__ == '__main__':
    unittest.main()
