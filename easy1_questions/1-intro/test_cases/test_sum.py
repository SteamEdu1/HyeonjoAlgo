import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.sum import addition

def test_example_1():
    assert addition(3, 2) == 5

def test_example_2():
    assert addition(-3, -6) == -9

def test_example_3():
    assert addition(7, 3) == 10
