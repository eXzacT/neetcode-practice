import pytest
from src.course_schedule import *

test_cases = [
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
    ((3, [[1, 0], [0, 2], [2, 1]]), False),
    ((3, [[0, 1], [0, 2], [1, 2]]), True),
    ((4, [[1, 0], [2, 1], [3, 2], [1, 3]]), False),
    ((20, [[0, 10], [3, 18], [5, 5], [6, 11], [
     11, 14], [13, 1], [15, 1], [17, 4]]), False),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_course_schedule(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
