#!/usr/bin/python3
"""Square Module
Private instance attribute: size.
Instantiation with size (no type/value verification).
"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initialize"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
