#!/usr/bin/python3
import json
import os


class FileStorage:
    """_summary_

    Returns:
        _type_: _description_
    """

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
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {
                k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()
            }
            FileStorage.__objects = obj_dict
            
    def delete(self, obj=None):
        """Deletes obj from __objects if it exists.

        Args:
            obj (optional): The object to delete from storage.
        """
        if obj is None:
            return

        obj_key = obj.__class__.__name__ + '.' + obj.id  # Create the key from class name and id
        if obj_key in self.__objects:
            del self.__objects[obj_key]  # Delete the object by its key


    def classes(self):
        """Returns a dictionary of valid classes and their references."""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return classes
