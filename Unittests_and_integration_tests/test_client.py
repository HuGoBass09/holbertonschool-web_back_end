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

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        """A method to test public_repos method"""
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}
        to_mock = "client.GithubOrgClient._public_repos_url"
        get_json_mock.return_value = [jeff, bobb, suee]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ["Jeff", "Bobb", "Suee"])
            self.assertEqual(x.public_repos("a"), ["Jeff"])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license, expected):
        """A method to test has_licence method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for github org client"""

    @classmethod
    def setUpClass(cls):
        """prepare for testing"""
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch("requests.get")
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """unprepare for testing"""
        cls.get_patcher.stop()
