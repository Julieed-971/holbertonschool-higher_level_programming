#!/usr/bin/python3
"""Student class."""


class Student:
    """Student class."""
    pass

    def __init__(self, first_name, last_name, age):
        """Initialize the student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Serialize the attributes of a class to a dictionnary."""
        if attrs is None:
            return vars(self)
        elif isinstance(attrs, list) and\
                all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student Instance."""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
