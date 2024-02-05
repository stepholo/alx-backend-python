#!/usr/bin/env python3
"""Module to define class TestAccessNestedMap"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class to define method to test access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict,
                               path: tuple, expected_result: any): -> None:
        """Method to test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    unittest.main()
