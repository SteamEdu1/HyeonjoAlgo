import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.hour_to_seconds import how_many_seconds

def test_example_1():
    assert how_many_seconds(2) == 7200

def test_example_2():
    assert how_many_seconds(10) == 36000

def test_example_3():
    assert how_many_seconds(24) == 86400