import unittest
from py_CLI_menus.object_return_menu import ObjectReturnMenu 

class TestObjectReturnMenu(unittest.TestCase):

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
        self.list_of_options_4 = [
            "CHOOSE Q",
            "CHOOSE Q",
            "CHOOSE Q",
            "CHOOSE Q"
        ]
        self.menu_header = "Select one of the following options: "
        self.menu_header_2 = "Choose Q this time: "

    def test_choose_first_option(self):

        string_menu = ObjectReturnMenu(self.list_of_options_1, self.menu_header)
        self.assertEqual("First Option - choose this", string_menu.choose())

    def test_choose_middle_option(self):

        string_menu = ObjectReturnMenu(self.list_of_options_2, self.menu_header)
        self.assertEqual("Second Option - choose this", string_menu.choose())

    def test_choose_last_option(self):

        string_menu = ObjectReturnMenu(self.list_of_options_3, self.menu_header)
        self.assertEqual("Fourth Option - choose this one", string_menu.choose())

    def test_choose_q(self):
        string_menu = ObjectReturnMenu(self.list_of_options_4, self.menu_header_2)
        self.assertEqual(None, string_menu.choose())

    def test_append_option(self):
        string_menu = ObjectReturnMenu(self.list_of_options_1, self.menu_header)
        self.list_of_options_1.append("New fifth option")
        self.assertEqual(5, len(string_menu.object_list))

    def test_confirm_loop(self):
        string_menu = ObjectReturnMenu(self.list_of_options_1, "Check y, n and other inputs to confirm work as expected: ")
        self.assertEqual("First Option - choose this", string_menu.choose(True))
