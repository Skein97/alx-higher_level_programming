#!/usr/bin/python3

"""Define a class Square that defines a square by: (based on 5-square.py)
    * Private instance attribute: size:
        ~property def size(self): to retrieve it
        ~ property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the message size must be >= 0
    * Private instance attribute: position:
        ~ property def position(self): to retrieve it
        ~ property setter def position(self, value): to set it:
            - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
    * Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    * Public instance method: def area(self): that returns the current square area
    * Public instance method: def my_print(self): that prints in stdout the square with the character #:
        ~ if size is equal to 0, print an empty line
        ~ position should be use by using space - Don’t fill lines by spaces when position[1] > 0
"""


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        self.size = size
        self.position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
