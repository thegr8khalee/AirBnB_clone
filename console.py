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
        try:
            class_name = args[0]
        except IndexError:
            pass


        if not args:
            print("** class name missing **")
        elif class_name not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
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
                #obj = storage.all()[key]

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
        }

        #User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
        args = arg.split('.')
        # args [user, update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")]
        clss = args[0]
        # clss = user
        args2 = args[1].split('(')
        # args2 = [update, "38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")]
        arg2 = args2[1].split(')')[0]
        # arg2 = ["38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John"]

        meth = args2[0]
        # meth = [update]
        temp = arg2.split(",")
        
        if meth in args_dict.keys():
            if meth != "update":
                return args_dict[meth]("{} {}".format(clss, arg2))
            else:
                cls_id = temp[0]
                cls_att = temp[1]
                cls_att_value = temp[2]
                return args_dict[meth]("{} {} {} {}".format(clss, cls_id, cls_att, cls_att_value))
        
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
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            things = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(things[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ to destroy an instance based on his ID: <class name>.destroy(<id>)."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    """ def do_update(self, arg):
        """
    "to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>)"""
    """args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** invalid class **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attr = args[2]
            attr_value = args[3]

            key = "{}.{}".format(class_name, instance_id)
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
            else:
                instance = objs[key]

                setattr(instance, attr, attr_value)
                storage.save() """
                


if __name__ == '__main__':
    HBNBCommand().cmdloop()