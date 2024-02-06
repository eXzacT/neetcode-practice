import pytest
from src.rotated_sorted_array_search import *

test_cases = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
    (([1, 2, 3, 4, 5, 6], 1), 0),
    (([1, 2, 3, 4, 5, 6], 6), 5),
    (([1, 2, 3, 4, 5, 6], 4), 3),
    (([1, 2, 3, 4, 5, 6], 2), 1),
    (([1, 2, 3, 4, 5, 6], 3), 2),
    (([1, 3], 3), 1),
    (([3, 1], 1), 1),
    (([5, 1, 3], 3), 2),
    (([3, 5, 1], 3), 0),
    (([4, 5, 6, 7, 0, 1, 2], 5), 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_rotated_sorted_array_search(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
