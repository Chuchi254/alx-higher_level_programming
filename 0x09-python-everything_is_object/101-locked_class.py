#!/usr/bin/python3
"""
This module prevents the user from dynamically creating new instance
"""


class LockedClass:
    """ preverts user from dynaimcally creating new instances"""
    __slots__ = ['first_name']
