#!/usr/bin/python3
"""magic class setup"""
import math


class MagicClass:
    """magic class setup"""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """docstring for area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """docstring for circumference"""
        return 2 * math.pi * self.__radius
