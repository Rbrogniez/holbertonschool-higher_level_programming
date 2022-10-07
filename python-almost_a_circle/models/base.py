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

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        jlist = []
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, "w+") as file:
                file.write("[]")

        elif list_objs:
            for i in list_objs:
                jlist.append(i.to_dictionary())

        st = cls.to_json_string(jlist)
        with open(filename, "w+") as myfile:
            myfile.write(st)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string or len(json_string) == 0:
            return []

        return json.loads(json_string)

