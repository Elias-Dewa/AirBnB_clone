#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from  models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
import pep8
from  models import storage
from  models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

    def setUp(self):
        """Sets up test methods."""
        pass    
    
    def test_place_instantiation(self):
        """Tests instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_place_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
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
