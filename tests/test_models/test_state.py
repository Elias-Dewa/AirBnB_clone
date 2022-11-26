#!/usr/bin/python3
"""Define unit test for state class"""


import unittest
from models.state import State
from models.base_model import BaseModel
import pep8


class TestStateClass(unittest.TestCase):
    """Representation of a set of tests for state class
    """

    def setUp(self):
        """set up the test
        """
        pass

    def test_pep8(self):
        """Test to check pycodestyle
        """
        py_code_style = pep8.StyleGuide(quiet=True)
        check = py_code_style.check_files(
            ['models/state.py', 'tests/test_models/test_state.py'])
        self.assertEqual(check.total_errors, 0, "Errors found")

    def test_is_instance(self):
        """Test to check that the user is instance
        """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

    def test_type_of_attributes(self):
        """Test to check the type of user attributes
        """
        state = State()
        self.assertTrue(type(state.name) == str)


if __name__ == '__main__':
    unittest.main()
