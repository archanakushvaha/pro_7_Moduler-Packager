import math


def square_root(number):
    if number < 0:
        return "Square root is not possible for negative number"

    return math.sqrt(number)


def power(number, exponent):
    return number ** exponent


def factorial(number):
    if number < 0:
        return "Factorial is not possible for negative number"

    return math.factorial(number)


def percentage(number, percent):
    return (number * percent) / 100


def circle_area(radius):
    return math.pi * radius * radius
