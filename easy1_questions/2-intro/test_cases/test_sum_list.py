import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.sum_list import sum_list

def test_example_1():
    assert sum_list([3, 4, 5]) == 12

def test_example_2():
    assert sum_list([20, 18, 16, 14, 17, 67]) == 152

def test_example_3():
    assert sum_list([7, 11, 12, 14]) == 44
