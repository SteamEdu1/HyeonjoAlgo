"""
Create a function that finds the hypotenuse of a triangle, 
when given two sides that are perpendicular to each other.

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

def hypotenuse(num1, num2):
    # This is the code for the hypotenuse
    inside_equation = num1 ** 2 + num2 ** 2
    hypotenuse =  math.sqrt(inside_equation)

    # This is to round the number by 1
    rounded_number = round(hypotenuse, 1)

    # return the rounded number
    return rounded_number