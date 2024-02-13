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
    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

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

    def default(self, arg):
        """
        retrieve all instances of a class by using: <class name>.all().
        """
        args_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count,
            "show": self.do_show
        }

        args = arg.split('.')
        clss = args[0]

        args2 = args[1].split('(')
        arg2 = args2[1].split(')')[0]


        meth = args2[0]
        

        if meth in args_dict.keys():
            return args_dict[meth]("{} {}".format(clss, arg2))
        
        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def do_count(self, arg):
        """Retrieve the number of instances of a class: <class name>.count()."""
        objs = storage.all()
        args = shlex.split(arg)

        if not args:
            print("** invalid command **")
            return

        clss = args[0]

        if clss not in self.valid_classes:
            print("** invalid class name **")
            return

        count = sum(1 for obj in objs.values() if obj.__class__.__name__ == clss)
        print(count)

    def do_show(self, arg):
        """ to retrieve an instance based on its ID: <class name>.show(<id>)."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** invalid class **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            things = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(things[key])
            else:
                print("** no instance found **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()