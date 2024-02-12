#!/usr/bin/python3
"""documented"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command int
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF reached"""
        print("")
        return True
    
    def emptyline(self):
        """do nothing """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()