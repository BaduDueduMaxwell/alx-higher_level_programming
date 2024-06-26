#!/usr/bin/python3
"""This containes an empty class called BaseGeometry"""


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
