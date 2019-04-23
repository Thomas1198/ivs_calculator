"""@file parser.py
@brief Expression parser.
"""

from main.modules.math import *


# priorities 3 ^√
#            2 /*
#            1 -+
def infixToPostfix(expr_infix):
    """

    @param expr_infix:
    @return:
    """
    priorities = {'/': 2, '*': 2, '-': 1, '+': 1, '^': 3, '√': 3}
    expr_postfix = list()
    stack = list()
    for element in expr_infix:
        if element not in ('/', '*', '-', '+', '^', '√'):
            expr_postfix.append(element)
        elif element in ('/', '*', '-', '+', '^', '√'):
            while not len(stack) == 0 and priorities[stack[-1]] > priorities[element]:
                expr_postfix.append(stack.pop())
            stack.append(element)

    while not len(stack) == 0:
        expr_postfix.append(stack.pop())

    return expr_postfix


def expresionStrToList(expr_str):
    """

    @param expr_str:
    @return:
    """
    expr_list = list()
    number = ""
    for c in expr_str:
        if c in "0123456789.":
            number = number + c
        elif c in "/*-+!^√":
            if len(number) != 0:
                if '.' in number:
                    expr_list.append(float(number))
                else:
                    expr_list.append(int(number))
                number = ""
            expr_list.append(c)
        else:
            # TODO add reaction on error
            print("Unknown operand/operator")

    if len(number) != 0:
        if '.' in number:
            expr_list.append(float(number))
        else:
            expr_list.append(int(number))
    return expr_list


def evalOneOperandOperators(expr_infix):
    """

    @param expr_infix:
    @return:
    """
    op = ['*', '/', '+', '-', '^', '√']
    res_list = []
    for i in range(len(expr_infix)):
        if i == 0:
            if expr_infix[i] == '√':
                res_list.append(square(expr_infix[i + 1]))
            elif expr_infix[i + 1] != '!':
                res_list.append(expr_infix[i])

        elif i == (len(expr_infix)) - 1:
            if expr_infix[i] == '!':
                res_list.append(factorial(expr_infix[i - 1]))
            elif expr_infix[i - 1] != '√':
                res_list.append(expr_infix[i])
            else:
                if expr_infix[i - 2] not in op:
                    res_list.append(expr_infix[i])

        elif expr_infix[i] == '!':
            res_list.append(factorial(expr_infix[i - 1]))

        elif expr_infix[i] == '√' and expr_infix[i - 1] in op:
            res_list.append(square(expr_infix[i + 1]))

        elif (expr_infix[i + 1] != '!') and (expr_infix[i - 1] != '√'):
            res_list.append(expr_infix[i])

        elif (expr_infix[i - 1] == '√') and (expr_infix[i - 2] not in op):
            res_list.append(expr_infix[i])

    return res_list


def evalExpr(postfixList):
    """

    @param postfixList:
    @return:
    """
    stack = list()
    for element in postfixList:
        if element not in ('/', '*', '-', '+', '^', '√'):
            stack.append(element)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = 0
            if element == '/':
                result = divide(op1, op2)
            elif element == '*':
                result = multiply(op1, op2)
            elif element == '-':
                result = subtract(op1, op2)
                print(result)
            elif element == '+':
                result = add(op1, op2)
            elif element == '^':
                result = power(op1, op2)
            elif element == '√':
                result = nth_root(op1, op2)
            else:
                # TODO add reaction on error
                print("Unknown operand/operator")
            stack.append(result)
    return stack[0]


def solve_expr(expr_str):
    """

    @param expr_str:
    @return:
    """
    expr_infix = expresionStrToList(expr_str)
    print("-LIST-", expr_infix)
    expr_infix = evalOneOperandOperators(expr_infix)
    print("-LIST2-", expr_infix)
    expr_postfix = infixToPostfix(expr_infix)
    print("-POSTFIX-", expr_postfix)
    print("EXPECTED:", eval(expr_str))
    return evalExpr(expr_postfix)
