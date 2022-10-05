#!/usr/bin/python3
"""Module Square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size,x,y,id)

