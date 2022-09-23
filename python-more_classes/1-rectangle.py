#!/usr/bin/python3
"""
Rectangle Module

"""


class Rectangle:

    """"Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self,value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        """retrieve height"""
        return self._height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
