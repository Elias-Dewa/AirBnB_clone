#!/usr/bin/python3

"""Define unit test for user class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUserClass(unittest.TestCase):
    """Representation of a set of tests for user class
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
            ['models/user.py', 'tests/test_models/test_user.py'])
        self.assertEqual(check.total_errors, 0, "Errors found")

    def test_is_instance(self):
        """Test to check that the user is instance
        """
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

    def test_type_of_attributes(self):
        """Test to check the type of user attributes
        """
        user = User()
        self.assertTrue(type(user.email) == str)
        self.assertTrue(type(user.password) == str)
        self.assertTrue(type(user.first_name) == str)
        self.assertTrue(type(user.last_name) == str)


if __name__ == '__main__':
    unittest.main()
