import pytest
from src.daily_temperatures import *

test_cases = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60], [1, 1, 1, 0]),
    ([30, 60, 90], [1, 1, 0]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_daily_temperatures(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
