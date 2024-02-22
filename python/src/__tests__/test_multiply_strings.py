import pytest
from src.multiply_strings import *

test_cases = [
    (("2", "3"), "6"),
    (("123", "456"), "56088"),
    (("9", "9"), "81"),
    (("9", "99"), "891"),
    (("999", "999"), "998001"),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_multiply_strings(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
