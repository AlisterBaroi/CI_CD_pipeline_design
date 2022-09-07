import unittest
import main

class TestMain(unittest.TestCase):
    def test_str(self):
        result = main.code1()
        x = self.assertEqual(result, str)
        if x != True:
            print( 'Test Fail Output: ', x)
        else:
            print( 'Test Pass Output: ', x)

