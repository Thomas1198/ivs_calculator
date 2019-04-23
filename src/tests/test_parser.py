import unittest

import sys
sys.path.insert(0,'..')
from main.modules.parser import solve_expr

class TestParser(unittest.TestCase):
    def test_simple_expressions(self):
        self.assertEquals(solve_expr("1+1"), 2)
        self.assertEquals(solve_expr("1-3"), -2)
        self.assertEquals(solve_expr("2*3"), 6)
        self.assertEquals(solve_expr("2^2"), 4)
        self.assertEquals(solve_expr("√4"), 2)
        self.assertEquals(solve_expr("4√625"), 5)
        self.assertEquals(solve_expr("4!"), 24)

    def test_faulty_expr(self):
        expressions = [
            "+", "-", "*", "/", "^", "/", "√", "!",
            "1+", "1-", "1*", "1/",
            "*1", "/1",
            "1++1", "1--1", "1**1", "1//1", "1^^1", "1√√1",
            "1/0", "1*1+",
        ]
        for expression in expressions:
            with self.assertRaises(ValueError):
                solve_expr(expression)

    def test_special_expr(self):
        expressions = {
            "+1": 1.0,
            "-1": -1.0,
            "2!!": 2.0,
            "1!!!": 1.0,
        }
        for k, v in expressions.items():
            self.assertEquals(solve_expr(k), v)

    def test_sequence_of_operators(self):
        expressions = {
            "1+1*2": 3.0,
            #"4√625^2": 25.0,
            "2!^2": 4.0,
            "2^2*4": 16.0,
            "4*2^2": 16.0,
            "2^2+4": 8.0,
            "4+2^2": 8.0,
        }
        for k, v in expressions.items():
            self.assertEquals(solve_expr(k), v)
        

if __name__ == '__main__':
    unittest.main()