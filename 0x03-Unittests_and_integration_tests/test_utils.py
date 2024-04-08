#!/usr/bin/env python3
""" unit tests for access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Mapping, Sequence, Any
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ This is the access nested map method test class """
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, map_dict: Mapping,
                               path: Sequence, result: Any):
        """ The access_nested_map test function"""
        self.assertEqual(access_nested_map(map_dict, path), result)

    @parameterized.expand([({}, {"a", }).
                           ({"a": 1}, {"a", "b"})])
    def test_access_nested_map_exception(self, map_dict: Mapping,
                                         path: Sequence):
        """ Testing the access_nested_map function for exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(map_dict, path)


class TestGetJson(unittest.TestCase):
    """ This is the Get Json test class """
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, url: str, payload: Dict):
        """ The get json test method """
        with patch("requests.get", mock_value=Mock(''{
                'json.return_value': payload})) as request_obj:
            response = get_json(url)
            self.assertEqual(response, payload)
            request_obj.assert_called_once_with(url)
