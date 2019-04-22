"""@file math.py
@brief Module for math calculations.
@author xchova20
@date 22.4. 2019
"""

from decimal import Decimal as D

def calculate(expr):
	return str(eval(expr))

def add(x, y):
	"""Adds two numbers.
	@param x first number.
	@param y second number.
	@return Decimal result
	"""
	return D(str(x)) + D(str(y))

def multiply(x, y):
	"""Multiplies two numbers.
	@param x first number.
	@param y second number.
	@return Decimal result
	"""
	return D(str(x)) * D(str(y))

def divide(x, y):
	"""Divides two numbers.
	@param x first number.
	@param y second number.
	@return Decimal result
	@exceptions ZeroDivisionError in case of second number being 0.
	"""
	if y == 0:
		raise ZeroDivisionError
	return D(str(x)) / D(str(y))

def subtract(x, y):
	"""SUbtracts two numbers.
	@param x first number.
	@param y second number.
	@return Decimal result
	"""
	return D(str(x)) - D(str(y))

def factorial(x):
	"""Creates a factorial.
	@param x first number, greater or equal to zero and integer.
	@return Decimal result
	@exceptions ValueError when x is not an integer or greater/equal to 0
	"""
	if not isinstance(x, int) or x < 0:
		raise ValueError("Factorial requires an integer greater or equal to 0")
	result = 1
	if x == 0:
		return 1
	return factorial(x * factorial(x-1))

def power(x, y):
	"""Raises number to a given power.
	@param x number.
	@param y power value.
	@return Decimal result
	"""
	return D(str(x)) ** D(str(y))

def square(x):
	"""Gives square root of a number.
	@@aram x number.
	@return Decimal result
	"""
	return D(str(x)) ** D(1/2)

def nth_root(x, y):
	"""Gives nth root of a number.
	@param x number.
	@param y n number
	@return Decimal result
	"""
	return D(str(x)) ** D(1/Decimal(str(y)))
