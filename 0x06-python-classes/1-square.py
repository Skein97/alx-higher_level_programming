#!/usr/bin/python3

"""A class Square that defines a square by: (based on 0-square.py)
    * Private instance attribute: size
    * Instantiation with size (no type/value verification)
    """


class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size):
        """Initialize method that stores the size of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size
