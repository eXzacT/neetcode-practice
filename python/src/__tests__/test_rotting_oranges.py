import pytest
from src.rotting_oranges import *

test_cases = [
    ([
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ], 4),
    ([
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ], -1),
    ([[0, 2]], 0),
    ([[1]], -1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_rotting_oranges(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
