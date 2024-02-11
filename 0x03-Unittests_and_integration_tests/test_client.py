#!/usr/bin/env python3
"""Module to define test cases for client methods"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class TestGithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        # Instantiate GithubOrgClient
        client = GithubOrgClient(org_name)

        # Define the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"

        # Call the org method
        result = client.org()

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the result is not None
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
