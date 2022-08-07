#!/usr/bin/python3

"""
    Defines a class Review.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Intializing the review class and passing arguments
        """
        super().__init__(**kwargs)
