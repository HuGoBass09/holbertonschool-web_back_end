#!/usr/bin/env python3
""" Unittests for client.py"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock, call
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Class to test GithubOrgClient"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, data, mock):
        """A method to test org function"""
        endpoint = "https://api.github.com/orgs/{}".format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """A method to test _public_repos_url property"""
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = "client.GithubOrgClient.org"
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("a")
            self.assertEqual(cli._public_repos_url, expected)
