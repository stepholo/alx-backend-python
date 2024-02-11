#!/usr/bin/env python3
"""Module to define test cases for client methods"""


import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )


if __name__ == '__main__':
    unittest.main()
