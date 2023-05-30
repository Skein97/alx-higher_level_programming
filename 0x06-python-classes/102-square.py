#!/usr/bin/python3

"""Defines a class Square.
"""


class Square:
    """ A class that defines a square by its size
    """
    def __eq__(self, other):
        """Method that checks equality
        """
        return self.__size == other.__size

    def __lt__(self, other):
        """Method that checks less than
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Method that checks less than or equal to
        """
        return self.__size <= other.__size

    def __ne__(self, other):
        """Method that checks not equal to
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """Method that checks greater than
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Method that checks greater than or equal to
        """
        return self.__size >= other.__size

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
