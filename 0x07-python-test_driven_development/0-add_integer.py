#!/usr/bin/python3
"""

This module has one function that adds up 2 integers

"""


def add_integer(a, b=98):
    """Return the sum of two integers or float as integers

       Args:
           a: first integer
           b: second integer
       Returns:
           Sum of the two integers
       Raises:
           TypeError: If either of the arguments not an integer or a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must an integer")

    return (int(a) + int(b))
