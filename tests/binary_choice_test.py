import unittest
from py_CLI_menus.binary_choice import binary_choice

class TestBinaryChoice(unittest.TestCase):

    def test_affirmative_response(self):
        self.assertEqual(True, binary_choice("Choose YES"))

    def test_negative_response(self):
        self.assertEqual(False, binary_choice("Choose NO"))

    def test_default_string(self):
        binary_choice()
        self.assertEqual(True, True)
