#!/usr/bin/env python3
"""Module to define class TestAccessNestedMap"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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



class TestGetJson(unittest.TestCase):
    """Class to test the utils json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Configure the mock to return a mock json method 
           with the test payload"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)



class TestMemoize(unittest.TestCase):
    """Class to test Memoize decoration"""
    class TestClass:
        """Class to define a method that returns a value"""
        def a_method(self):
            """Method that returns a value"""
            return 42

        @memoize
        def a_property(self):
            """Method to define the main method"""
            return self.a_method()

    @patch('test_utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        """Test the memoize decorator"""
        mock_a_method.return_value = 42
        obj = self.TestClass()

        result1 = obj.a_property
        result2 = obj.a_property

        # mock_a_method.assert_called_once()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
