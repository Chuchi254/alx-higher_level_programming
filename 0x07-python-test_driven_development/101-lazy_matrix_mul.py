#!/usr/bin/python3
"""Provides a function to multiply 2 matrices using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplytw matrices using NumPy"""
    return np.matmul(m_a, m_b)
