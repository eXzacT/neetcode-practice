import pytest
from src.burst_baloons import *

test_cases = [
    ([3, 1, 5, 8], 167),
    ([3, 1, 5, 8, 9, 5, 4, 2, 1], 834),
    ([1, 5], 10),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_burst_baloons(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
