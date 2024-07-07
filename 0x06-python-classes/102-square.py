#!/usr/bin/python3
""" Amodule that defines a square."""


class Square:
    """
    This class defines a square with a private instance attribute
    for size.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.


        Args:
            value (float or int): The size of the square.

        Raises:
            ThpeError: If size is not an number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """ Override the default Equals behavior to compare square areas """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """ Override the default Not Equals to compare square areas. """
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __lt__(self, other):
        """ Override the default Less Than to compare square areas. """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """ Override the default Less Than or equals to
        compare square areas. """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """ Override the default Greater than to
        compare square areas. """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """ Override the default Greater Than or
        Equals to compare square areas. """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
