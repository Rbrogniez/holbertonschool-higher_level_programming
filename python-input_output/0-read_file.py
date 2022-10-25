#!/usr/bin/python3
"""Module Read file"""


def read_file(filename=""):
    """
    Function Read a file
    """
with open(filename, "r+",encoding='utf-8') as file:
    print(file.readlines())
    file.close()
