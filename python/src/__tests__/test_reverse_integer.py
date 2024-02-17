import pytest
from src.reverse_integer import *

test_cases = [
    (321, 123),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0),
    (-2147483648, 0),
    (-2147483412, -2143847412),
    (1563847412, 0),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_reverse_integer(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
