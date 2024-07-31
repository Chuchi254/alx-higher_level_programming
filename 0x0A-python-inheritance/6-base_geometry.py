#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method"""


class BaseGeometry:
    """A class repreenting base geometry"""
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented
        """
        raise Exception("area() is not implemented")
