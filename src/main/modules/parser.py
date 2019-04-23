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

def expresionToList(expresion):
    res_list = list()
    number = ""
    for c in expresion:
        if c in "0123456789.":
            number = number + c
        elif c in "/*-+!^√":
            if len(number) != 0:
                res_list.append(float(number))
                number = ""
            res_list.append(c)

    if len(number) != 0:
        res_list.append(float(number))
    return res_list


def solve_expr(expresion_str):
    print(expresion_str)
    expresion = expresionToList(expresion_str)
    print(expresion)
    return 0
