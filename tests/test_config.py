import unittest
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