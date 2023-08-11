#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import shlex
import models
import cmd
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "Place": Place, "Review": Review, "State": State}


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Function that do EOF"""
        return True

    def do_quit(self, line):
        """Function that close the program"""
        return True

    def do_create(self, arg):
        """Create a new instace of basemodel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints ths string representation of an
instace based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name"""
        args = shlex.split(arg)
        lt_obj = []
        if len(args) == 0:
            for value in models.storage.all().values():
                lt_obj.append(str(value))
            print("[", end="")
            print(", ".join(lt_obj), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    lt_obj.append(str(models.storage.all()[key]))
            print("[\"" + ", ".join(lt_obj) + "\"]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attributes"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
