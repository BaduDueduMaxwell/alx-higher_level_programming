#!/usr/bin/python3
"""writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as file:
        content = json.dump(my_obj, file)
    return content
