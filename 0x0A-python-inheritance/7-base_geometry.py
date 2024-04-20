#!/usr/bin/python3
"""This program validates an integer"""


class BaseGeometry:
    """
    Base class for geometry.

    Public instance method:
        def area(self): Raises an Exception with the message
                        'area() is not implemented'.
    """
    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise Exception("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
