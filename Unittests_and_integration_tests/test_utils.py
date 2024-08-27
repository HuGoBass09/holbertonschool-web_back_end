#!/usr/bin/env python3
""" Unittests for utils.py"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class to test access_nested_map function"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, result):
        """A method to test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """A method to test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test get_json function"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """A method to test get_json function"""
        with patch("utils.requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Class to test memoize decorator"""

    def test_memoize(self):
        """A method to test memoize decorator"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method

        with patch.object(TestClass, "a_method") as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
