import pytest
from src.coin_change_best import *

test_cases = [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([7, 5, 10], 23), -1),
    (([1], 0), 0),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_coin_change(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
