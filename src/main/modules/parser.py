"""@file parser.py
@brief Expression parser.
"""
import math

def organ_operations(text):
	"""Organize operations in list.
	@param text input string text.
	@return list of operations result.
	"""
	op = ['*','/','+','-','!','^','√']
	oper_input = []
	for i in range(len(text)):
		if text[i] in op:
			oper_input.append(text[i])
	return oper_input

def organ_number(text):
	"""Organize numbers in list.
	@param text input string text.
	@return list of numbers result.
	"""
	op = ['*','/','+','-','!','^','√']
	number_input = []
	number = ''
	for i in range(len(text)):
		if (text[i] in op)!=1:
			number += text[i]
		else:
			number_input.append(number)
			number = ''
	number_input.append(number)
	return number_input

def solve_expr(expression):
	operations = []
	numbers = []
	operations = organ_operations(expression)
	numbers = organ_number(expression)
	#TODO
	return 0 #TODO
