import pytest
from src.jump_game import *

test_cases = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([2, 0], True),
    ([0], True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_jump_game(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
