import unittest
import main

class TestMain(unittest.TestCase):
    def test_str(self):
        result main.code1()
        self.assertEqual(result, str)

# type(text1) == int 