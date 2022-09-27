#!/usr/bin/python3
"""
Module is kind of class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class ;
    otherwise False."""
    if isinstance(obj, (int,float)) or issubclass(a_class, (int,float)):
        return (True)
    else:
        return(False)

