#!/usr/bin/python3
"""
Module inherts from
"""


def is_kind_of_class(obj, a_class):
    """unction that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False."""
    if issubclass(obj, a_class):
        return (True)
    else:
        return (False)
