#!/usr/bin/python3
# 6-square.py by kode
"""A module that defines a square"""


class Square:
    """Represents a square with its size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the private position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private position attribute, ensuring it's a valid tuple"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square's area"""
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
