import pytest
from src.redundant_connection import *

test_cases = [
    ([[1, 2], [1, 3], [2, 3]], (2, 3)),
    ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], (1, 4)),
    ([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]], (1, 3)),
    ([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]], (2, 5)),
    ([[7, 8], [2, 6], [2, 8], [1, 4], [9, 10], [1, 7],
     [3, 9], [6, 9], [3, 5], [3, 10]], (3, 10)),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_redundant_connection(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
