#!/usr/bin/python3

class base:()

__nb_objects = 0

def __init__(self, id=None):
    if id is not None:
        self.__id = id
    else:
        __nb_objects +1


