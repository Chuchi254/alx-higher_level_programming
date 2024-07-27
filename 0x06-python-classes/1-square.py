#!/usr/bin/python3
""" A module that defines a square."""


class Square:
    """
    This class defines a square with a private instance
    attributing for size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
