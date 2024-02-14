import pytest
from src.sliding_window_max import *

test_cases = [
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
    (([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5]),
    (([1], 1), [1]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_sliding_window_max(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
