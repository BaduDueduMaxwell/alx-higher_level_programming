#!/usr/bin/python3
"""Define a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class inherits from int"""

    def __eq__(self, other):
        """Override equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operator"""
        return super().__eq__(other)
