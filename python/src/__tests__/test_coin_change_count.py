import pytest
from src.coin_change_count import *

test_cases = [
    ((5, [1, 2, 5]), 4),
    ((3, [2]), 0),
    ((10, [10]), 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_coin_change_count(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
