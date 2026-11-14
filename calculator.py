"""
calculator.py
- Defines functions used to create a simple calculator
Repository: https://github.com/ikshajoshii-art/lab11-IJ-AA

Partner 1: Iksha Joshi
Partner 2: Aryan Akirha
One function per operation, in order.
"""
# First examp"""
# calculator.py
# - Defines functions used to create a simple calculator
#
# One function per operation, in order.
# """
# # First example
#
# import math
#
# def square_root(a):
#     if a < 0:
#         raise ValueError("Cannot calculate square root of a negative number")
#     return math.sqrt(a)
#
#
# def hypotenuse(a, b):
#     return math.hypot(a, b)
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     if a == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return b/a
#
#
# def logarithm(a, b):
#     if a <= 0 or b <= 0 or b == 1:
#         raise ValueError("Invalid logarithm arguments")
#     return math.log(a, b)
#
#
# def exponent(a, b):
#     return a ** ble

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a


def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid logarithm arguments")
    return math.log(a, b)


def exponent(a, b):
    return a ** b



