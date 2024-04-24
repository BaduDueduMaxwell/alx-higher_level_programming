#!/usr/bin/python3
"""This module returns the JSON representation of an obj"""
import json


def from_json_string(my_str):
    """Returns the JSON of an obj"""
    return json.loads(my_str)
