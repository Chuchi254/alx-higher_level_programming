#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new line after
each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    i = 0
    result = ""

    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    lines = [line.strip() for line in result.split('\n')]
    print("\n".join(lines), end="")
