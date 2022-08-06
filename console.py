#!/usr/bin/python3
""" console that contains the entry point """

import cmd
from models.base_model import Basemodel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
import re

class HBNBCommand(cmd.Cmd):
    """console"""
    prompt = "(hbnb) "
    @classmethod
    def fetch_command(cls, command):
        """Gets the command typed in the console"""
        commands = {"all": cls.do_all, "show": cls.do_show, "destroy": cls.do_destroy,
        "update": cls.do_update, "count": cls.do_count}
        if command in commands:
            return commands[command]
        else:
            return None

    def do_EOF(self, arg):
        """Quit the program"""
        return True

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def emptyline(self):
        """ do nothing """
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()