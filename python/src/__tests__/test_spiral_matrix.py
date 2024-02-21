import pytest
from src.spiral_matrix import *

test_cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[6, 9, 7]], [6, 9, 7]),
    ([[7], [9], [6]], [7, 9, 6]),
    ([[1, 2], [3, 4]], [1, 2, 4, 3]),
    ([[2, 5], [8, 4], [0, -1]], [2, 5, 4, -1, 0, 8]),

]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_spiral_matrix(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
