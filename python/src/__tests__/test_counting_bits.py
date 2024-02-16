import pytest
from src.counting_bits import *

test_cases = [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_counting_bits(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
