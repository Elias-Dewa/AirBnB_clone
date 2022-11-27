#!/usr/bin/python3

"""Define unit test for review class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReviewClass(unittest.TestCase):
    """Representation of a set of tests for review class
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
            ['models/review.py', 'tests/test_models/test_review.py'])
        self.assertEqual(check.total_errors, 0, "Errors found")

    def test_is_instance(self):
        """Test to check that the user is instance
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

    def test_type_of_attributes(self):
        """Test to check the type of user attributes
        """
        review = Review()
        self.assertTrue(type(review.place_id) == str)
        self.assertTrue(type(review.user_id) == str)
        self.assertTrue(type(review.text) == str)


if __name__ == '__main__':
    unittest.main()
