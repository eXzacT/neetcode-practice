import pytest
from src.product_of_array_except_self import *

test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([0, 0], [0, 0]),
    ([0, 4, 0], [0, 0, 0])
]

functions = [globals()[name]
             for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_product_of_array_except_self(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
