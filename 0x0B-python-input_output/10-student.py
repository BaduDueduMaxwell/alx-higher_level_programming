#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Initialization of attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict description with data for JSON serialization"""
        if attrs is None:
            return self.__dict__
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict
