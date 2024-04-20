#!/usr/bin/python3
"""Add attribute to object if possible"""


def add_attribute(obj, attr_name, attr_value):
    """Add attribute to object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
