#!/usr/bin/python3
"""This module defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class of a Square that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of instances"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self. width)

    def display(self):
        """prints square with #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    @property
    def size(self):
        """getter for width size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for width size"""
        self.__width = value
