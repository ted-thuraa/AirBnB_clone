#!/usr/bin/python3

"""
    Defines a class City.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Intializing the City class and passing arguments
        """
        super().__init__(**kwargs)
