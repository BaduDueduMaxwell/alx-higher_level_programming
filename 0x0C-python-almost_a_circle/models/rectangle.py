#!/usr/bin/python3
from models.base import Base
"""This module defines a Rectangle class that inherits from Base class"""


class Rectangle(Base):
    """Rectangle class inherits Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)