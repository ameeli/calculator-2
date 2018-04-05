"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def run_calculator_2():
    run_function = True

    while run_function:
        user_input = raw_input('>')

        if user_input == 'q' or user_input == 'quit':
            run_function = False

        else:
            calculator_2(user_input)

def check_input(user_input)
    
def calculator_2(inputs):
    equation = inputs.split(' ')

    if len(equation) == 3:
        try:
            operator = equation[0]
            num1 = float(equation[1])
            num2 = float(equation[2])
        except:
            return "please follow formatting guidelines"

    elif len(equation) == 2:
        try:
            operator = equation[0]
            num1 = float(equation[1])
        except:
            return "please follow formatting guidelines"

    else:
        return "please follow fornatting guidelines"


    if operator == '+':
        if len(equation) == 2:
            return "please follow formatting guidelines"
        return add(num1, num2)

    elif operator == '-':
        return subtract(num1, num2)

    elif operator == '*':
        return multiply(num1,num2)
    
    elif operator == '/':
        return divide(num1, num2)

    elif operator == 'square':
        return square(num1)

    elif operator == 'cube':
        return cube(num1)

    elif operator == 'pow':
        return power(num1, num2)

    elif opertor == 'mod':
        return mod(num1, num2)



