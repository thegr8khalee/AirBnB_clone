#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Command int"""
    prompt = "(hbnb)"
    
    def do_quit(self, arg):
        """enter quit or exit to quit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF..."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()