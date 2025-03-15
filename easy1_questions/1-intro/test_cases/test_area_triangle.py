import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.area_triangle import tri_area

def test_example_1():
    assert tri_area(3, 2) == 3

def test_example_2():
    assert tri_area(7, 4) == 14

def test_example_3():
    assert tri_area(10, 10) == 50

def test_extra_1():
    assert tri_area(7, 10) == 35
