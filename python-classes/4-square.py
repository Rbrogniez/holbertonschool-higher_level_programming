#!/usr/bin/python3
"""Square Module
Private instance attribute: size.
Instantiation with size (no type/value verification).
"""


class Square:

    """Square Class"""

    def __init__(self, size=0):
        """Initialize"""
        self.__size = size

    @property
    def size(self):
        "retrieve suze"
        return self.__size

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("size must be an integrer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """Square of area"""
        return self.__size
