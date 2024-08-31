#!/usr/bin/python3
"""The module defines a function 'read_file' that reads a text file
and prints its contents to stdout."""


def read_file(filename=""):
    """Function reads the contents of a text file and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents)
