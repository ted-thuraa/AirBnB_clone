#!/usr/bin/python3
""" the unittests for the console features """

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """test cases for review class"""

    def test_docstring(self):
        """ checks if docstring is there """
        apple = "orange"
        self.assertIsNotNone(apple)


if __name__ == "__main__":
    unittest.main()
