#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """
    Command int
    """
    prompt = "(hbnb)"

    valid_classes = ["BaseModel"]

    