import pytest
from src.last_stone_weight import *

test_cases = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([1], 1),
    ([7, 6, 7, 6, 9], 3),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_last_stone_weight(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
