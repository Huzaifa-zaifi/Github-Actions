
import pytest
from grading import calculate_grade

def test_grade_a():
    assert calculate_grade(95) == "A"

def test_grade_b():
    assert calculate_grade(85) == "B"

def test_grade_c():
    assert calculate_grade(75) == "C"

def test_grade_d():
    assert calculate_grade(65) == "D"

def test_grade_f():
    assert calculate_grade(40) == "F"

def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_grade(105)
