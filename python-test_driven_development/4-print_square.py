#!/usr/bin/python3
"""
This is print square module
"""


def print_square(size):
    """
    Print square with size and
    print error if size is not an int > 0

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size <= 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for x in range(size):
                print("#", end="")
            print()
