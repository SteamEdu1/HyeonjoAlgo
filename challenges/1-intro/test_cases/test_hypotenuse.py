import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.hypotenuse import hypotenuse

def test_example_1():
    assert hypotenuse(8, 10) == 12.8

def test_example_2():
    assert hypotenuse(5, 7) == 8.6

def test_example_3():
    assert hypotenuse(9, 2) == 9.2