#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object if possible
"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it's possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
