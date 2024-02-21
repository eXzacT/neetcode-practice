import pytest
from src.happy_number import *

test_cases = [
    (19, True),
    (10, True),
    (2, False),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_happy_number(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
