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
from models import storage
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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves to a JSON file,
        and prints the ID when finished """

        if arg:
            try:
                new_instance = models.dummy_classes[arg]
                new_instance = new_instance()
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name misssing **")

    def do_show(self, arg):
        """Prints the string representation of an instance,
        if given the class name and id """

        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        print(models.storage.all()[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id and saves changes"""
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        deleted = models.storage.all().pop(key)
                        del(deleted)
                        models.storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """ Prints a string of all instances or if given the class name,
        of just the instances of the class name """
        # print all values in the storage.all() if no paremeters entered
        # otherwise print only values that match parameters entered
        result = []
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                for instance, obj in models.storage.all().items():
                    if instance.split('.')[0] == arg[0]:
                        result.append(str(obj))
            else:
                for instance, obj in models.storage.all().items():
                    result.append(str(obj))
            if result:
                print(result)

    def do_update(self, arg):
        """ Updates an instance based on the class name and ID.
        Adds or updates attributes ans saves the changes """
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        instance = models.storage.all()[key]
                        if len(arg) > 2:
                            if len(arg) > 3:
                                setattr(instance, arg[2], arg[3].strip('"'))
                                instance.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_count(self, arg):
        """ counts number of objects of specified class """
        count = 0
        if args:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                for instance, obj in models.storage.all().items():
                    count += 1
            else:
                print("** class doesn't exist **")
        else:
            for instance, obj in models,storage.all().items():
                count += 1
        print(count)

    def default(self, line):
        """
        handle invalid commands and
        special commands like <class name>.<command>()
        """
        match = re.fullmatch(r"[A-Za-Z]+\.[A-Za-z]+\(.*?\)", line)
        if match:
            splitted = line.split('.')


if __name__ == '__main__':
    HBNBCommand().cmdloop()