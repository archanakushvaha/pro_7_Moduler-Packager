import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def logarithm(number, base=10):
    if number <= 0:
        return "Logarithm is possible only for positive numbers"
    return math.log(number, base)
