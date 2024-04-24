#!/usr/bin/python3
import json
"""This module returns the JSON representation of an obj"""


def to_json_string(my_obj):
    """Returns the JSON of an obj"""
    return json.dumps(my_obj)
