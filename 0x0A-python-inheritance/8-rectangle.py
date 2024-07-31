#!/usr/bin/python3
"""Defines a class Rectangle thaat inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle"""
    def __init__(self, width, height):
        """Initialize a new Rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
