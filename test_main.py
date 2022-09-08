import unittest
import main

class TestMain(unittest.TestCase):
    def test_str(self):
        result = main.code1()
        return self.assertEqual(result, str)
        
    def test_str(self):
        result = main.test()
        return self.assertEqual(result, 't')
