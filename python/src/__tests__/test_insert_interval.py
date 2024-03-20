import pytest
from src.insert_interval import *

test_cases = [
    (([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
    (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
     [[1, 2], [3, 10], [12, 16]]),
    (([[4, 5], [6, 9]], [1, 2]), [[1, 2], [4, 5], [6, 9]]),
    (([[4, 5], [6, 9]], [10, 15]), [[4, 5], [6, 9], [10, 15]]),
    (([], [4, 5]), [[4, 5]]),
    (([[1, 5]], [2, 3]), [[1, 5]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_insert_interval(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
