#!/usr/bin/python3
"""This module returns dict description with simple\
data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dict description with data for JSON serialization"""
    return obj.__dict__
