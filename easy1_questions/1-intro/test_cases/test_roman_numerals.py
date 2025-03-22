import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from questions.roman_numerals import converter

def test_example_1():
    assert converter("X") == 10

def test_example_2():
    assert converter("IV") == 4

def test_example_3():
    assert converter("III") == 3

def test_extra_1():
    assert converter("XXXIX") == 39

def test_extra_2():
    assert converter("XXIX") == 29

def test_extra_3():
    assert converter("XIV") == 14

def test_extra_4():
    assert converter("XXVII") == 27
