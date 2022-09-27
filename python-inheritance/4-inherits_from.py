#!/usr/bin/python3
"""
Module inherts from
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited from the specified clas"""
    if issubclass(obj, a_class):
        return (True)
    else:
        return (False)
