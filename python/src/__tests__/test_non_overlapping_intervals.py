import pytest
from src.non_overlapping_intervals import *

test_cases = [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
    ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_non_overlapping_intervals(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
