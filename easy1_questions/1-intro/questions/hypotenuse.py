"""
Create a function that finds the hypotenuse of a triangle, 
when give two sides that are perpendicular to each other.

the function must round the result to 1 decimal place.

Examples:
    hypotenuse(8, 10) ➞ 12.8
    hypotenuse(5, 7) ➞ 8.6
    hypotenuse(9, 2) ➞ 9.2

Rounding Example:
    number = 34.14559

    # rounds number to 2 decimal places
    rounded_number = round(number, 2)

    print(rounded_number) 
"""
import math

def hypotenuse(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    rounded_number = round(hypotenuse, 1)

    # return rounded number
    return rounded_number

