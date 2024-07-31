#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_same(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_at_start(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_with_float(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_with_mixed(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_with_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_with_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a'])


if __name__ == '__main__':
    unittest.main()
