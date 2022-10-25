#!/usr/bin/python3
"""Module Student"""


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs:
            dic = {}
            for x in self.__dict__:
                if x in attrs:
                    dic[x] = self.__dict__[x]
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes"""
        for x in json:
            self.__dict__[x] = json[x]
