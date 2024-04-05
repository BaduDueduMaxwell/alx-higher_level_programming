#!/usr/bin/python3
# 2-square.py by kode
"""A module that defines a square """


class Square:
    """Represents a square shape with its size"""
    def __init__(self, size=0):
        """Initializing this square object
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size
