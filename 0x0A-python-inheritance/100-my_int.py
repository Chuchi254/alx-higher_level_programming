#!/usr/bin/python3
"""Defines a class MyInt that inherits from int with inverted == and !=
operators
"""


class MyInt(int):
    """A class representing a rebellious integer"""
    def __eq__(self, other):
        """Override the equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator"""
        return super().__eq__(other)
