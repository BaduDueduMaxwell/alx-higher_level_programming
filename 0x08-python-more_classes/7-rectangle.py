#!/usr/bin/python3
"""Represents a class that defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle with properties for width and height,
    methods to get and set them, calculate area and perimeter.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes objects.

        Args:
            width: width of rectangle
            height: height of rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (0 if width or height is 0).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle using "#".

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join("#" * self.__width for _ in range(self.__height)))

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Return a string representataion of the rectangle when deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
