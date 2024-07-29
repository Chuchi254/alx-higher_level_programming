#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """Defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height

        @property
        def width(self):
            """Gets the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Gets the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the heihgt of the rectanle."""
            if not isinstance(value, int):
                raise TypeError("heihgt must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
