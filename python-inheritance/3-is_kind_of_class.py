#!/usr/bin/python3

import re


def is_kind_of_class(obj, a_class):
    if isinstance(obj,int):
        return (True)
    elif issubclass(a_class,int):
        return (True)
    else:
        return(False)

