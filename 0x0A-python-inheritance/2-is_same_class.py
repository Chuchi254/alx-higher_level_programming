#!/usr/bin/python3
"""Provides a function to check if an object is exactly an instance of a
a specified class.
"""


def is_same_class(obj, a_class):
    """True if obj is exactly an instance of a_class, otherwise False"""
    return type(obj) is a_class
