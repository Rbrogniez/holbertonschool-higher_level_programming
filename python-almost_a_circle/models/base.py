#!/usr/bin/python3
"""
Module Base Classe
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0



    def __init__(self, id=None):

        """if id is not None, assign the public instance attribute id with this
        argument value
        otherwise, increment __nb_objects and assign the new value to the public
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
