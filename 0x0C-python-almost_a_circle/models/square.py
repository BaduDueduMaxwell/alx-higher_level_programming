#!/usr/bin/python3
"""This module defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class of a Square that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of instances"""
        super().__init__(size, size, x, y, id)

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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Replaces attributes of square class"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
