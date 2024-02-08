import pytest
from src.permutations import *

test_cases = [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_permutations(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        # To make the order not matter
        assert sorted(func(test_input)) == sorted(expected)
