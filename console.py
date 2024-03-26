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
import re
import ast


def eval_curls(temp):
    """_summary_

    Args:
        temp (_type_): _description_
    """
    curls = re.search(r"\{(.*?)\}", temp)

    if curls:
        id_c = shlex.split(temp[: curls.span()[0]])
        id_d = [ix.strip(",") for ix in id_c][0]
        string_input = curls.group(1)
        try:
            dict_input = ast.literal_eval("{" + string_input + "}")
        except Exception:
            print("** dictionary not valid **")
            return
        return id_d, dict_input
    else:
        args = temp.split(",")
        try:
            id_d = args[0]
            attr_name = args[1]
            attr_value = args[2]
            return "{}".format(id_d), "{} {}".format(attr_name, attr_value)
        except Exception:
            print("** no args found **")


class HBNBCommand(cmd.Cmd):
    """
    Command int fav egv  tev tb e v etb
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
        key = class_name + "." + instance_id
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
                if key.split(".")[0] == args[0]:
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

        objj = storage.all()
        if not args:
            print("** class name missing **")
        elif class_name not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])

            if key not in objj:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                curls = re.search(r"\{(.*?)\}", arg)

                if curls:
                    string_input = curls.group(1)
                    dict_input = ast.literal_eval("{" + string_input + "}")
                    att_names = list(dict_input.keys())
                    att_values = list(dict_input.values())

                    att_name1 = att_names[0]
                    att_value1 = att_values[0]

                    att_name2 = att_names[1]
                    att_value2 = att_values[1]

                    setattr(storage.all()[key], att_name1, att_value1)
                    setattr(storage.all()[key], att_name2, att_value2)
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    # obj = storage.all()[key]

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
        """EOF... v tr b vet vwet gb ewgtwe"""
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

        # User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
        args = arg.split(".")
        # args [user, update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")]
        clss = args[0]
        # clss = user
        args2 = args[1].split("(")
        # args2 = [update, "38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")]
        arg2 = args2[1].split(")")[0]
        # arg2 = ["38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John"]

        meth = args2[0]
        # meth = [update]
        # temp = arg2.split(",")"""

        if meth in args_dict.keys():
            if meth != "update":
                return args_dict[meth]("{} {}".format(clss, arg2))
            else:
                object_id_d, dictionary_arg = eval_curls(arg2)
                try:
                    if isinstance(dictionary_arg, str):
                        attt = dictionary_arg
                        return args_dict[meth](
                            "{} {} {}".format(clss, object_id_d, attt)
                        )
                    elif isinstance(dictionary_arg, dict):
                        dict_attt = dictionary_arg
                        return args_dict[meth](
                            "{} {} {}".format(clss, object_id_d, dict_attt)
                        )
                except Exception:
                    print("** no args **")

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
        """to retrieve an instance based on its ID: <class name>.show(<id>)."""
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
        """to destroy an instance based on his ID: <class name>.destroy(<id>)."""
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

    """def do_update(self, arg):
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
                try:
                    instance_id = args[1]
                    instance = storage.get(class_name, instance_id)
                    if instance is None:
                        print("** no instance found **")
                        return
                
                # Parse dictionary representation
                    dict_representation = ' '.join(args[2:])
                    try:
                        dict_representation = eval(dict_representation)
                    except Exception as e:
                        print("** invalid dictionary representation:", e)
                        return
                
                    if not isinstance(dict_representation, dict):
                        print("** invalid dictionary representation: must be a dictionary **")
                        return

                # Update instance attributes
                    for attr, value in dict_representation.items():
                        setattr(instance, attr, value)
                
                    storage.save()
                except Exception as e:
                    print("** update error:", e)"""

    """def eval_curls(temp):
        
        
        if curls:
            id_c = shlex.split(temp[:curls.span()[0]])
            id_d = [ix.strip(",") for ix in id_c][0]
            string_input = curls.group(1)
            try:
                dict_input = ast.literal_eval("{" + string_input + "}")
            except Exception:
                print("** dictionary not valid **")
                return
            return id_d, dict_input
        else:
            args = temp.split(",")
            try:
                id_d = args[0]
                attr_name = args[1]
                attr_value = args[2]
                return "{}".format(id_d), "{} {}".format(attr_name, attr_value)
            except Exception:
                print("** no args found **")"""


if __name__ == "__main__":
    """ lorem sdhjbcd qc c cr crcqw cd"""
    HBNBCommand().cmdloop()
