#!/usr/bin/python3
"""Module Square"""


from curses.textpad import rectangle


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
