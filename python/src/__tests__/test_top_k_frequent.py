import pytest
from src.top_k_frequent import *

test_cases = [
    (([5, 3, 1, 1, 1, 3, 73, 1], 2), [1, 3]),
    (([5, 3, 1, 1, 1, 3, 73, 1], 1), [1]),
    (([5, 3, 1, 1, 1, 3, 73, 1], 0), []),
]

functions = [globals()[name] for name in dir() if 'top_k_frequent' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_top_k_frequent(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
