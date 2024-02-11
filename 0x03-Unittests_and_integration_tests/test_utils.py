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
                               path: tuple, expected_result: any) -> None:
        """Method to test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict,
                               path: tuple, expected_result: any) -> None:
        """Method to test if equal to """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
        ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple,
                                         expected_exception_msg: str) -> None:
        """Method to test access_nested_map execption"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_exception_msg)


if __name__ == '__main__':
    unittest.main()
