#!/usr/bin/python3
import json
import os
#from datetime import datetime
from models.base_model import BaseModel
#from models.user import user
#import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utc-8") as file:
                    self.__objects = json.load(file)
            except Exception:
                pass

