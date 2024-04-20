#!/usr/bin/python3
"""Check if obj is an instance of a class that\
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
      Check if obj is an instance of a class that inherited\
(directly or indirectly) from the specified class.
      Args:
          obj: The object to be checked.
          a_class: The class to compare against.

      Returns:
          True if the obj is an instance of a class that inherited
(directly or indirectly), False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
