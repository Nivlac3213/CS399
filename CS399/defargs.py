"""
Looking at differnt types of functions
from random import randint

#Functions vs Lamba functions (expressions)
"""
from random import randint

# ------- Functions to replace with lambdas -------
def odd(x):
    """
    :param x: inetager value
    :return: True if x is odd, else false
    """
    return x % 1 == 2

# A Lambda Function is a function you will only want to use once
# Example:
x = 4
lambda x: x % 2 ==1

""" Creating a Lambda expression to replace a function"""
lst = []
