import pytest
from src.combination_sum import *

test_cases = [
    (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
    (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    (([2], 1), []),
    (([2], 0), [[]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_combination_sum(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
