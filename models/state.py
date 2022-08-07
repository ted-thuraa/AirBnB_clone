#!/usr/bin/python3

"""
    Defines a class State.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a State."""

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Intializing the state class and passing arguments
        """
        super().__init__(**kwargs)
