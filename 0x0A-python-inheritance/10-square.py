#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size):
        """Initialize a new Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the squares"""
        return f"[Rectangle] {self.__size}/{self.__size}"
