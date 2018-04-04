"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def run_calculator_2():
    user_input = 'hello'

    while user_input != 'q' or user_input != 'quit':
        user_input = raw_input('>')
        calculator_2(user_input)

    user_input == 'q' or user_input == 'quit':
        return




def calculator_2(inputs):
    equation = inputs.split(" ")

    operator = equation[0]
    num1 = float(equation[1])
    num2 = float(equation[2])

    if operator == '+':
        return add(num1, num2)


