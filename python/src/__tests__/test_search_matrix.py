import pytest
from src.search_matrix import *

test_cases = [
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 100), False),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11), True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_search_matrix(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
