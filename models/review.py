#!/usr/bin/python3
"""Define review class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public instance of review class
    """
    place_id = ""
    user_id = ""
    text = ""
