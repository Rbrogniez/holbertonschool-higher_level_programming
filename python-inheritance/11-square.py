#!/usr/bin/python3
"""Module Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'

