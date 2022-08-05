#!/usr/bin/evn python3
"""
base classs for the entireproject
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Custom base for all the classes in the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """
    def __int__(self, *args, **kwargs):
        """Public instance artributes initialization after creation
        ==================
        *args(args): arguments list (not used)
        **kwargs(dict): dictionary of arguments to creat an object
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(uuid4())
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if (key != '__class__'):
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            """models.storage.new(self)"""

    def __str__(self):
        """
        Returns string representation of the class
        """
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()
        """models.storage.save()"""
    def to_dict(self):
        """
        Method returns a dictionary containing all
        keys/values of __dict__ instance
        """
        class_dict = self.__dict__.copy()
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': datetime.isoformat(self.created_at)})
        class_dict.update({'updated_at': datetime.isoformat(self.updated_at)})
        return class_dict
