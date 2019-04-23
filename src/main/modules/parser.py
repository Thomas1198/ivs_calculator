"""@file parser.py
@brief Expression parser.
"""

from main.modules.math import *


# priorities 3 ^√
#            2 /*
#            1 -+
def infixToPostfix(expresions):
    priorities = {'/': 2, '*': 2, '-': 1, '+': 1, '^': 3, '√': 3}
    postFixList = list()
    stack = list()
    for element in expresions:
        if element not in ('/', '*', '-', '+', '^', '√'):
            postFixList.append(element)
        elif element in ('/', '*', '-', '+', '^', '√'):
            while not len(stack) == 0 and priorities[stack[-1]] > priorities[element]:
                postFixList.append(stack.pop())
            stack.append(element)

    while not len(stack) == 0:
        postFixList.append(stack.pop())

    return postFixList


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
        else:
            # TODO add reaction on error
            print("Unknown operand/operator")

    if len(number) != 0:
        res_list.append(float(number))
    return res_list


def fact_square(text):
    op = ['*','/','+','-','^','√']
    newText = []
    for i in range(len(text)):
        if i == 0:
            if text[i] == '√':
                newText.append(square(text[i + 1]))
            elif text[i + 1] != '!':
                newText.append(text[i])

        elif i == (len(text)) - 1:
            if text[i] == '!':
                newText.append(factorial(int(text[i - 1])))
            elif text[i - 1] != '√':
                newText.append(text[i])
            else:
                if text[i-2] not in op:
                    newText.append(text[i])

        elif text[i] == '!':
            newText.append(factorial(int(text[i - 1])))

        elif text[i] == '√' and text[i-1] in op:
            newText.append(square(text[i + 1]))

        elif (text[i + 1] != '!') and (text[i - 1] != '√'):
            newText.append(text[i])

        elif (text[i-1] == '√') and (text[i-2] not in op):
            newText.append(text[i])

    return newText


def final(text):
  op = ['*','/','+','-','^','√']
  stack = []
  for i in text:
    if i not in op:
      stack.append(i)
      continue

    x, y = stack.pop(), stack.pop()
    if i == '+':
      stack.append(add(x, y))
    elif i == '-':
      stack.append(substract(x, y))
    elif i == '*':
      stack.append(multiply(x, y))
    elif i == '/':
      stack.append(divide(x, y))
    elif i == '^':
      stack.append(power(x, y))
    elif i == '√':
      stack.append(nth_root(x, y))
    #NEED FIX
  return stack


def solve_expr(expresion_str):
    expresion_infix = expresionToList(expresion_str)
    print("-LIST-", expresion_infix)
    expresion_infix = fact_square(expresion_infix)
    print("-LIST2-", expresion_infix)
    expresion_postfix = infixToPostfix(expresion_infix)
    print("-POSTFIX-", expresion_postfix)
    postfix = final(expresion_postfix)
    print("-final-", postfix)
    return postfix
