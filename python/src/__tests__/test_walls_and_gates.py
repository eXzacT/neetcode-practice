import pytest
from src.walls_and_gates import *

test_cases = [
    ([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
     [0, -1, 2147483647, 2147483647]], [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
    ([[2147483647, -1, 0], [-1, -1, -1], [2147483647, 2147483647, 2147483647]],
     [[2147483647, -1, 0], [-1, -1, -1], [2147483647, 2147483647, 2147483647]])
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_walls_and_gates(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
