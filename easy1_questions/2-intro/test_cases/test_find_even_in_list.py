import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.find_even_in_list import first_even

def test_example_1():
    assert first_even([1, 2, 3]) == 2

def test_example_2():
    assert first_even([1, 3, 45, 7, 10]) == 10

def test_example_3():
    assert first_even([7, 11, 12, 14]) == 12
