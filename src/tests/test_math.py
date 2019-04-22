import unittest

import sys
sys.path.insert(0,'..')
from main.modules.math import (
    add, subtract, multiply, divide, factorial, square, nth_root)

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(1, 1), 2)
        self.assertEquals(add(-4, 1), -3)
        self.assertEquals(add(0, 0), 0)
        self.assertEquals(add(5.5, 1), 6.5)

    def test_subtract(self):
        self.assertEquals(subtract(2, 1), 1)
        self.assertEquals(subtract(-3, -1), -2)
        self.assertEquals(subtract(-3, 1), -4)
        self.assertEquals(subtract(0, 0), 0)
        self.assertEquals(subtract(12.5, 2), 10.5)

    def test_multiply(self):
        self.assertEquals(multiply(2, 1), 2)
        self.assertEquals(multiply(15, 10), 150)
        self.assertEquals(multiply(-3, -1), 3)
        self.assertEquals(multiply(-3, 1), -3)
        self.assertEquals(multiply(0, 0), 0)
        self.assertEquals(multiply(8.5, 2), 17)

    def test_divide(self):
        self.assertEquals(divide(2, 1), 2)
        self.assertEquals(divide(10, 2), 5)
        self.assertEquals(divide(20, -10), -2)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        self.assertEquals(divide(0, 5), 0)

    def test_factorial(self):
        self.assertEquals(factorial(1), 1)
        self.assertEquals(factorial(0), 1)
        self.assertEquals(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-2)
        with self.assertRaises(ValueError):
            factorial(2.4)

    def test_square(self):
        self.assertEquals(square(1), 1)
        self.assertEquals(square(4), 2)
        self.assertEquals(square(0), 0)
        self.assertEquals(square(10), 3.1622776601683795)
        with self.assertRaises(ValueError):
            factorial(-2)

    def test_nth_root(self):
        self.assertEquals(nth_root(1, 2), 1)
        self.assertEquals(nth_root(625, 4), 5)
        self.assertEquals(nth_root(625, -4), 0.2)
        with self.assertRaises(ValueError):
            nth_root(-2, 2)
        with self.assertRaises(ZeroDivisionError):
            nth_root(10, 0)
        


if __name__ == '__main__':
    unittest.main()