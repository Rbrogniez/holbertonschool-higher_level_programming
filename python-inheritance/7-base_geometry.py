#!/usr/bin/python3
"""
Module Base Geometry
"""


class BaseGeometry:
    """Class Base Geometry"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

