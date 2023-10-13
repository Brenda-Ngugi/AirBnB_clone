#!/usr/bin/env python3
"""
"""
import json
import ast


class FileStorage():
    """serialize instances to a JSON and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in objects"""
        new_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[new_name] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(FileStorage.__file_path, "r") as f:
                data_dict = json.load(f)
                for key, value in data_dict.items():
                    """safely evaluate the string back into a Python object"""
                    class_value = value["__class__"]
                    del value["__class__"]
                    FileStorage.__objects[key] = eval(class_value + "(**value)")
        except FileNotFoundError:
            pass
