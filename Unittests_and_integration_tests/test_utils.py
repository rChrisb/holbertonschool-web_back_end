#!/usr/bin/env python3

"""unit tests"""


import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({"a": 1}, ["b"]),
        ({"a": {"b": 2}}, ["a", "c"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json
        """
        class Mocked(Mock):
            """
            Mocked class
            """

            def json(self):
                """
                Mocked json method
                """
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test memoize
    """

    def test_memoize(self):
        """
        test memoize
        """

        class TestClass:
            """
            Test class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()


if __name__ == '__main__':
    unittest.main()
