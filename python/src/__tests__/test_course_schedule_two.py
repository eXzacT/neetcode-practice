import pytest
from src.course_schedule_two import *

test_cases = [
    ((2, [(1, 0)]), [[0, 1]]),
    ((4, [(1, 0), (2, 0), (3, 1), (3, 2)]), ([0, 2, 1, 3], [0, 1, 2, 3])),
    ((1, []), [[0]]),
    ((3, [[1, 0], [1, 2], [0, 1]]), [[]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_course_schedule_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) in expected
