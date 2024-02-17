import pytest
from src.reverse_bits import *

test_cases = [
    (0b00000010100101000001111010011100, 964176192),
    (0b11111111111111111111111111111101, 3221225471),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_reverse_bits(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
