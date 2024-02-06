import pytest
from src.find_minimum_in_rotated_sorted_array import *

test_cases = [
    ([1, 2, 3, 4, 5], 1),
    ([5, 1, 2, 3, 4], 1),
    ([2, 3, 4, 5, 1], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([4, 5, 1, 2, 3], 1),
    ([2, 1], 1),
    ([11, 13, 15, 17], 11),
    ([100]+[num for num in range(1, 100)], 1),
    ([num for num in range(2, 100)]+[1], 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_find_minimum_in_rotated_sorted_array(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
