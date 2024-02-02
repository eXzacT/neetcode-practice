import pytest
from src.longest_consecutive_sequence import *

test_cases = [
    ([1, 2, 0, 1], 3),
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([0, 3, 7, 4], 2),
    ([0, 3, 7, 5], 1),
    ([], 0),
    ([0, -1], 2),
    ([1], 1),
    # ([num for num in range(1000)], 1000),
    # ([num for num in range(0, 1000, 2)], 1)
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_longest_consecutive_sequence(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
