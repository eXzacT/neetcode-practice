import pytest
import copy
from src.rotate_image import *

test_cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("matrix,expected", test_cases)
def test_rotate_image(matrix, expected):
    print(f"\nFor input {matrix}")
    for func in functions:
        matrix_copy = copy.deepcopy(matrix)
        func(matrix_copy)
        assert matrix_copy == expected
