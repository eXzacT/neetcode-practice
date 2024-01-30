import pytest
from src.two_sum import *

test_cases = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
]

functions = [globals()[name] for name in dir() if 'two_sum' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_two_sum(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
