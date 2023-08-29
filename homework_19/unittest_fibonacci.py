import unittest

from homework_19 import Fibonacci


class TestFibonacci(unittest.TestCase):

    def test_positive_int(self):
        fibonacci_calculator = Fibonacci()
        result = fibonacci_calculator(5)
        self.assertIsInstance(result, int)

    def test_negative_int(self):
        with self.assertRaises(ValueError):
            fibonacci_calculator = Fibonacci()
            fibonacci_calculator(-5)

    def test_str(self):
        with self.assertRaises(ValueError):
            fibonacci_calculator = Fibonacci()
            fibonacci_calculator("5")

    def test_empty(self):
        with self.assertRaises(TypeError):
            fibonacci_calculator = Fibonacci()
            fibonacci_calculator()


if __name__ == '__main__':
    unittest.main()
