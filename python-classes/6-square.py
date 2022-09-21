#!/usr/bin/python3
"""Square Module
Private instance attribute: size.
Instantiation with size (no type/value verification).
"""


class Square:

    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Square of area"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):

                for x in range(self.position[0]):
                    print("", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()


