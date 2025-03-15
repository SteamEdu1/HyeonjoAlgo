import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.increment import addition

def test_example_1():
    assert addition(0) == 1

def test_example_2():
    assert addition(9) == 10

def test_example_3():
    assert addition(-3) == -2