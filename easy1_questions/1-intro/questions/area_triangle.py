"""
Write a function that takes the base and height of a triangle and return its area (int)


Examples
    tri_area(3, 2) ➞ 3
    tri_area(7, 4) ➞ 14
    tri_area(10, 10) ➞ 50
"""

def tri_area(base, height):
    return int(height * base / 2)