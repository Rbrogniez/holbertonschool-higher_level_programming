#!/usr/bin/python3
"""
This is add integer module
"""


def add_integer(a, b=98):
    """
    Return the addition of 2 integers or
    error if not int or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
