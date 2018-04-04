"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def caculator_2():
    user_input = raw_input('>')

    if user_input == 'q' or user_input == 'quit':
        return

    else:
        equation = user_input.split(" ")

        if equation[0] ==

