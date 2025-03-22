import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.return_remainder import remainder

def test_example_1():
    assert remainder(1, 3) == 1

def test_example_2():
    assert remainder(3, 4) == 3

def test_example_3():
    assert remainder(5, 5) == 0

def test_example_4():
    assert remainder(7, 2) == 1