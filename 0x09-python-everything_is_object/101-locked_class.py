#!/usr/bin/python3
"""
This module prevents the user form dynamically creating new instance
"""


class LockedClass:
    __slots__ = ['first_name']
