#!/usr/bin/python3
"""

"""


def __init__(self, width=0, height=0):
    self.__width = width
    self.__height = height

@property
def width(self):
    return self.__width

@width.setter
def width(self,value):
    if type(width) is not int:
        raise TypeError("width must be an integer")
    elif type(width) < 0:
        raise ValueError("width must be >= 0")


@property
def height(self):
    return self._height


