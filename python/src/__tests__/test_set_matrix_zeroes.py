import pytest
import copy
from src.set_matrix_zeroes import *

test_cases = [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
     [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ([[1, 0, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [1, 0, 1]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("matrix,expected", test_cases)
def test_set_matrix_zeroes(matrix, expected):
    print(f"\nFor input {matrix}")
    for func in functions:
        matrix_copy = copy.deepcopy(matrix)
        func(matrix_copy)
        assert matrix_copy == expected
