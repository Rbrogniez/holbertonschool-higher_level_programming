#!/usr/bin/python3
"""
Module Write to a file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "a+") as file:
        file.write(text)
        return len(text)
