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

    def to_json(self):
        """Serialize the attributes of a class to a dictionnary."""
        attributes = vars(self)
        return attributes
