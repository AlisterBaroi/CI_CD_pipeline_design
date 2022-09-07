import unittest
import main

class TestMain(unittest.TestCase):
    def test_str(self):
        result = main.code1()
        x = self.assertEqual(result, str)
        print( 'Test Output: ', x)
