#!/usr/bin/python3
# 4-square.py by kode
"""A module that defines a square"""


class Square:
    """Represents a square with its size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieves the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private size attribute, ensuring it's a valid integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square's area"""
        return self.size ** 2

    def my_print(self):
        if self.size < 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
