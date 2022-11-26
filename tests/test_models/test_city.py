#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
import pep8
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def test_city_instantiation(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))        

    def test_city_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)            
            
   def test_pep8(self):
        """Test to check pycodestyle
        """
        py_code_style = pep8.StyleGuide(quiet=True)
        check = py_code_style.check_files(
            ['models/user.py', 'tests/test_models/test_user.py'])
        self.assertEqual(check.total_errors, 0, "Errors found")

if __name__ == "__main__":
    unittest.main()
