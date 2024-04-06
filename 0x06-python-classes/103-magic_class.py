#!/usr/bin/python3
"""magic class setup"""
import math


class MagicClass:
    """magic class setup"""
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius
