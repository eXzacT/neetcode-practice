import pytest
from src.largest_rectangle_in_histogram import *

test_cases = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([1, 1], 2),
    ([2, 1, 2], 3),
    ([3, 6, 5, 7, 4, 8, 1, 0], 20),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_largest_rectangle_in_histogram(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
