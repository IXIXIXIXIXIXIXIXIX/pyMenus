import unittest
from menus.string_menu import StringMenu

class TestStringMenu(unittest.TestCase):

    def setUp(self):

        self.list_of_options_1 = [
            "First Option - choose this",
            "Second Option",
            "Third Option",
            "Fourth Option"
        ]

        self.list_of_options_2 = [
            "First Option",
            "Second Option - choose this",
            "Third Option",
            "Fourth Option"

        ]
        self.list_of_options_3 = [
            "First Option",
            "Second Option",
            "Third Option",
            "Fourth Option - choose this one"
        ]
        self.menu_header = "Select one of the following options:"

    def test_choose_first_option(self):

        string_menu = StringMenu(self.list_of_options_1, self.menu_header)
        self.assertEqual(0, string_menu.choose())
