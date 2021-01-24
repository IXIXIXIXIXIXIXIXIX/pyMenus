import unittest
from py_CLI_menus.int_return_menu import IntReturnMenu

class TestIntReturnMenu(unittest.TestCase):

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
        self.menu_header = "Select one of the following options: "
        self.menu_header_2 = "Choose Q this time: "

    def test_choose_first_option(self):

        string_menu = IntReturnMenu(self.list_of_options_1, self.menu_header)
        self.assertEqual(0, string_menu.choose())

    def test_choose_middle_option(self):
        string_menu = IntReturnMenu(self.list_of_options_2, self.menu_header)
        self.assertEqual(1, string_menu.choose())

    def test_choose_last_option(self):
        string_menu = IntReturnMenu(self.list_of_options_3, self.menu_header)
        self.assertEqual(3, string_menu.choose())

    def test_choose_q(self):
        string_menu = IntReturnMenu(self.list_of_options_3, self.menu_header_2)
        self.assertEqual(None, string_menu.choose())

    def test_append_option(self):
        string_menu = IntReturnMenu(self.list_of_options_1, self.menu_header)
        self.list_of_options_1.append("New fifth option")
        self.assertEqual(5, len(string_menu.object_list))

    def test_confirm_loop(self):
        string_menu = IntReturnMenu(self.list_of_options_1, "Check y, n and other inputs to confirm work as expected: ")
        self.assertEqual(0, string_menu.choose(True))
