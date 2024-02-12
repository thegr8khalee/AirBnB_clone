#!/usr/bin/python3
"""
console for the airbnb clone program
"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Command int
    """
    prompt = "(hbnb)"

    valid_classes = ["BaseModel", "User"]

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{args[0]}()")
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance name missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")


    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        
        objects = storage.all()

        del objects[key]
        storage.save()


    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        """
        args = shlex.split(arg)
        objects = storage.all()
        if len(args) == 0:
            for key, value in objects.items():
                print(str(value))
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        args = shlex.split(arg)
        class_name = args[0]


        if not args:
            print("** class name missing **")
        elif class_name not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = class_name + '.' + args[1]

            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else: 
                attr_name = args[2]
                attr_value = args[3]
                obj = storage.all()[key]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                setattr(storage.all()[key], attr_name, attr_value)
                storage.save()

    def do_quit(self, arg):
        """enter quit or exit to quit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF..."""
        print()
        return True
    
    def emptyline(self):
        """
        Do nothing when an empty line is passed
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()