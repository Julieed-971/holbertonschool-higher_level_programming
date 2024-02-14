#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_to_json_file = __import__('6-load_from_json_file').load_from_json_file

input = sys.argv[1:]

try:
    file_data = load_to_json_file("add_item.json")
except FileNotFoundError:
    file_data = []

input_list = file_data + input

save_to_json_file(input_list, "add_item.json")
