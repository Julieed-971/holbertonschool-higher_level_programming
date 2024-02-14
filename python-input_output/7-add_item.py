#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""
import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

def add_item(input):
    list = list(input())
    with open("add_item.json", "w") as f:
        save.f
        return load.f
