#!/usr/bin/python3
"""This module returns the JSON representation of an obj"""


import json
def to_json_string(my_obj):
    """Returns the JSON of an obj"""
    return json.dumps(my_obj)
