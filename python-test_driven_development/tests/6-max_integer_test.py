#!/usr/bin/python3
"""Unittest for max_integer([..])

This module contains unit tests for the `max_integer` function from the
`6-max_integer` module.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_positive_numbers(self):
        """Test list with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test list with mixed positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_duplicates(self):
        """Test a list with duplicate values."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_all_same_negative(self):
        """Test a list with all elements being the same negative value."""
        self.assertEqual(max_integer([-7, -7, -7, -7]), -7)

    def test_floats(self):
        """Test a list with floating point numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_mixed_types(self):
        """Test a list with mixed integer and float values."""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1, -2.2, 3, -4.4]), 3)

    def test_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')

    def test_single_string(self):
        """Test a single string (considered as an iterable of characters)."""
        self.assertEqual(max_integer('hello'), 'o')

    def test_none(self):
        """Test None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        """Test max_integer with no argument."""
        with self.assertRaises(TypeError):
            max_integer()


if __name__ == '__main__':
    unittest.main()
