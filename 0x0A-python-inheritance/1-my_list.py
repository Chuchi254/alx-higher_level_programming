#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Subclass of list has a method to print the list in sorted order"""
    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
