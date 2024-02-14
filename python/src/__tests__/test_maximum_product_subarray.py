import pytest
from src.maximum_product_subarray import *

test_cases = [
    ([2, 3, -2, 4], 6),
    ([2, 3, -2, 10], 10),
    ([1, 3, 5, -1, 2, 7, -11, 0, -11], 2310),
    ([-2, 0, -1], 0),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_maximum_product_subarray(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
