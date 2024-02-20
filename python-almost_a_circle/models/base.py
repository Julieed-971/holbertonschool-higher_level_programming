#!/usr/bin/python3
"""Base class for the full project"""
import json


class Base:
    """Base class for the full project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None or len(list_objs) <= 0:
            list_objs = "[]"
            filename = f"{cls.__name__}.json"
            with open(filename, "w") as f:
                f.write(list_objs)
        else:
            filename = f"{cls.__name__}.json"
            json_list = []
            with open(filename, "w") as f:
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    json_list.append(obj_dict)
                json_str = cls.to_json_string(json_list)
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation"""
        if json_string is None or len(json_string) <= 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            new_inst = cls(1)
        new_inst.update(**dictionary)
        return new_inst
