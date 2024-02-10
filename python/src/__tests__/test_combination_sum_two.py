import pytest
from src.combination_sum_two import *

test_cases = [
    (([10, 1, 2, 7, 6, 1, 5], 8), [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]),
    (([2, 5, 2, 1, 2], 5), [
        [1, 2, 2],
        [5]
    ]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_combination_sum_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert sorted(func(*test_input)) == expected
