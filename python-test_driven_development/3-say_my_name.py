#!/usr/bin/python3
"""
This print name and last name module
"""


def say_my_name(first_name, last_name=""):
    """
    return first name or last name or error if not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
