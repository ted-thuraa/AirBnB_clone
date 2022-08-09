#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re






class HBNBCommand(cmd.Cmd):
    

    

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves to a JSON file,
        and prints the ID when finished  """


            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Display the string of class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

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
        Adds  """
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

        """Display str representations of instances of a given class"""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


    def default(self, line):
        """
        handle invalid commands and
        special commands 
        """
        match = re.fullmatch(r"[A-Za-Z]+\.[A-Za-z]+\(.*?\)", line)
        if match:
            splited = line.split('.')
            if splited[0] in models.dummy_classes:
                parsed = splited[1].split("(")
                parsed[1] = parsed[1].strip(")")
                args = parsed[1].split(",")
                args = [arg.strip() for arg in args]
                if len(args) >= 3:
                    temp = args[2]
                    args = [arg.strip('"') for arg in args[:2]]
                    args.append(temp)
                else:
                    args = [arg.strip('"') for arg in args]
                command = self.fetch_command(parsed[0])
                if command:
                    reconstructed_args = [arg for arg in args]
                    reconstructed_args.insert(0, splited[0])
                    reconstructed_command = " ".join(reconstructed_args)
                    command(self, reconstructed_command)
                else:
                    print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
