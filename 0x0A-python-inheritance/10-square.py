#!/usr/bin/python3
"""This program inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class"""
    def __init__(self, size):
        """Initializes size of square"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
