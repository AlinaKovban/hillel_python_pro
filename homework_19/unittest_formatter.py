import unittest

from for_testing import formatted_name


class TestFormatter(unittest.TestCase):

    def test_string(self):
        result = formatted_name("First", "Last", "Middle")
        self.assertIsInstance(result, str)

    def test_one_is_int(self):
        with self.assertRaises(TypeError):
            formatted_name(1, "Last")

    def test_one_is_list(self):
        with self.assertRaises(TypeError):
            formatted_name("First", ["Last", "Last1"])

    def test_one_is_tuple(self):
        with self.assertRaises(TypeError):
            formatted_name("First", "Last", ("Middle", "Middle1"))

    def test_first_empty_value(self):
        with self.assertRaises(ValueError):
            formatted_name("", "Last", "Middle")

    def test_last_empty_value(self):
        result = formatted_name("First", "Last")
        expect = formatted_name("First", "Last", "")
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
