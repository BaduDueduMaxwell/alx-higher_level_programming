#!/usr/bin/python3
"""This function checks if an obj of instance or obj is instance of a class"""


def is_kind_of_class(obj, a_class):
    """
      This function checks if an obj of instance or obj is instance of a class
      Args:
          obj: The object to be checked.
          a_class: The class to compare against.

      Returns:
          True if the obj is an exact instance of the class, False otherwise.
    """
    return isinstance(obj, a_class)
