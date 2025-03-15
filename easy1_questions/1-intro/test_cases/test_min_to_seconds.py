import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.min_to_seconds import convert

def test_example_1():
    assert convert(5) == 300

def test_example_2():
    assert convert(3) == 180

def test_example_3():
    assert convert(2) == 120