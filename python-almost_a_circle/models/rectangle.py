#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):

    """ Class Rectangle with inherits Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inizializes a Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def display(self):
        """Returns the display"""
        for width in range(self.__height):
            for length in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} {self.__width}/{self.__height}'
