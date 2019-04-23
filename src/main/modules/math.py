##
# @file math.py
# @brief Module for math calculations.
# @author xchova20
# @date 22.4. 2019


from decimal import Decimal as D


def calculate(expr):
    return str(eval(expr))

## 
# Adds two numbers.
# @param x first number.
# @param y second number.
# @return float result
def add(x, y):
    return float(D(str(x)) + D(str(y)))

##
# Multiplies two numbers.
# @param x first number.
# @param y second number.
# @return float result
def multiply(x, y):
    return float(D(str(x)) * D(str(y)))

##
# Divides two numbers.
# @param x first number.
# @param y second number.
# @return float result
# @exception ZeroDivisionError in case of second number being 0.
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return float(D(str(x)) / D(str(y)))

##
# SUbtracts two numbers.
# @param x first number.
# @param y second number.
# @return float result
def subtract(x, y):
    return float(D(str(x)) - D(str(y)))

##
# Creates a factorial.
# @param x first number, greater or equal to zero and integer.
# @return float result
# @exception ValueError when x is not an integer or greater/equal to 0
def factorial(x):
    if not isinstance(x, int) or x < 0:
        raise ValueError("Factorial requires an integer greater or equal to 0")
    if x == 0:
        return 1
    return x * factorial(x - 1)


##
# Raises number to a given power.
# @param x number.
# @param y power value.
# @return float result
def power(x, y):
    return float(D(str(x)) ** D(str(y)))


##
# Gives square root of a number.
# @param x number greater or equal to 0.
# @return float result
# @exception ValueError when x is not greater or equal to 0
def square(x):
    if x < 0:
        raise ValueError
    return float(D(str(x)) ** D(1 / 2))


##
# Gives nth root of a number.
# @param x number greater or equal to 0.
# @param y n number, cannot be 0
# @return float result
# @exception ValueError when x is not greater or equal to 0
# @exception ZeroDivisionError when y is 0
def nth_root(x, y):
    if x < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return float(D(str(x)) ** D(1 / D(str(y))))
