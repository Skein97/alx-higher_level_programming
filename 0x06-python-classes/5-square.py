#!/usr/bin/python3

"""Define a class Square that defines a square by: (based on 4-square.py)

    * Private instance attribute: size:
        ~ property def size(self): to retrieve it
        ~ property setter def size(self, value): to set it:
            -size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the message size must be >= 0
    * Instantiation with optional size: def __init__(self, size=0):
    * Public instance method: def area(self): that returns the current square area
    * Public instance method: def my_print(self): that prints in stdout the square with the character #:
        ~ if size is equal to 0, print an empty line
"""


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
