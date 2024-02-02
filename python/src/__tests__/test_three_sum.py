import pytest
from src.three_sum import *

test_cases = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([1, -1, -1, 0], [[-1, 0, 1]]),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_three_sum(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
