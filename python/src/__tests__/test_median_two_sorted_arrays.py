import pytest
from src.median_two_sorted_arrays import *

test_cases = [
    (([1, 3], [2]), 2),
    (([1, 2], [3, 4]), 2.5),
    (([], [1]), 1),
    (([], [2, 3]), 2.5),
    (([3], [-2, -1]), -1),
    (([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]), 0),
    (([2, 3], [1]), 2),
    (([1, 2, 3], [1, 2]), 2),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_median_two_sorted_arrays(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
