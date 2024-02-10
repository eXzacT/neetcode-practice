import pytest
from src.find_duplicate_ll import *

test_cases = [
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([3, 1, 3, 4, 2, 5], 3),
    ([2, 2, 2, 2, 2], 2),
]
functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_find_duplicate_ll(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
