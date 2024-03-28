import pytest
from src.maximum_sum_subarray import *

test_cases = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-1], -1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_maximum_subarray(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
