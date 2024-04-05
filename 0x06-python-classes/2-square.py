#!/usr/bin/python3
# 2-square.py by kode
"""Defines a square """


class Square:
    """defines a sqr based on 1-square.py"""
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
        self.__sized = size
