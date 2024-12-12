import unittest
import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import Config

class TestConfig(unittest.TestCase):
    def test_development_config(self):
        self.assertTrue(Config.Development.DEBUG)
        self.assertEqual(Config.Development.PORT, 8000)
        
    def test_production_config(self):
        self.assertFalse(Config.Production.DEBUG)
        self.assertEqual(Config.Production.PORT, 80)
        
    def test_app_version(self):
        self.assertEqual(Config.VERSION, "1.0.0")

if __name__ == '__main__':
    unittest.main()