#!/usr/bin/python3
"""Write an Object to a text file"""
import json

def save_to_json_file(my_obj, filename):
    """Write an Object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
