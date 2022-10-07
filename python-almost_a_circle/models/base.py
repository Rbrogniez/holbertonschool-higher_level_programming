#!/usr/bin/python3
"""
Module Base Classe
"""

from fileinput import filename
import json
from queue import Empty


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """if id is not None, assign the public instance attribute id with this
        argument value
        otherwise, increment _nb_objects and assign the new value to the public
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def to_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

