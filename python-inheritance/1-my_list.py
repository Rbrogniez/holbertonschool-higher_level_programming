#!/usr/bin/python3
"""
Module My list
"""


class MyList(list):
    """My List Class"""
    def print_sorted (self):
        """ prints the list, but sorted """
        print (sorted(self))
