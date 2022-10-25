#!/usr/bin/python3
"""
Rectangle Module

"""


class Rectangle:

    """"Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Initialize"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (self.__height + self.__width)*2

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        s = ('#' * self.__width + '\n') * self.__height
        return s[:-1]

    def __repr__(self):
        """Return an official string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

