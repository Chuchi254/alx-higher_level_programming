#!/usr/bin/python3
"""
This module provides a function to multiply 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the result."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must e a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_length = len(m_a[0])
    for row in m_a:
        if len(row) != row_length:
            raise TypeError("each row of m_a must be of the same size")
    row_length = len(m_b[0])
    for row in m_b:
        if len(row) != row_length:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            element_sum = 0
            for k in range(len(m_b)):
                element_sum += m_a[i][k] * m_b[k][j]
            row_result.append(element_sum)
        result.append(row_result)

    return result
