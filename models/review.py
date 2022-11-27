#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a Review class"""
=======

"""Define review class that inherits from BaseModel class
"""
>>>>>>> 2361ce354722f490ddd70eeaa6ee7bababa9faf7

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
