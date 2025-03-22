import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.debug_1 import cubes

def test_example_1():
    assert cubes(3) == 27

def test_example_2():
    assert cubes(5) == 125

def test_example_3():
    assert cubes(10) == 1000