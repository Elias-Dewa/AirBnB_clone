#!/usr/bin/python3
"""Define city class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Public instance of city class
    """
    state_id = ""
    name = ""
