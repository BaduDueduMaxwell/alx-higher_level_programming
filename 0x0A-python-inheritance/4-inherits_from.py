#!/usr/bin/python3
"""This function checks if an obj of instance or obj is instance of a class that inherited(directly or indirectly)"""


def inherits_from(obj, a_class):
    """
      This function checks if an obj of instance or obj is instance of a class that inherited(directly or indirectly)
      Args:
          obj: The object to be checked.
          a_class: The class to compare against.

      Returns:
          True if the obj is an instance of a class that inherited(directly or indirectly), False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
