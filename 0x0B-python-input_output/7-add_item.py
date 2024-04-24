#!/usr/bin/python3
"""This module adds all arguments to a Python list and\
 save them to a file"""
import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    if path.exists(filename):
        try:
            my_list = load_from_json_file(filename)
        except json.decoder.JSONDecodeError:
            my_list = []
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)
