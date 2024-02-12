#!/usr/bin/python3
"""
Console module containing the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
