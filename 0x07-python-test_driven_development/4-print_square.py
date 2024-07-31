#!/usr/bin/python3
"""
This module provides a function to print a square with the character #.
"""


def print_square(size):
    """
    Print a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
