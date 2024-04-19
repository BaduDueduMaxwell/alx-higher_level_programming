#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """method to sort the list"""
    def print_sorted(self):
        print(sorted(self))
