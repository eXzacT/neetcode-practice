import pytest
from src.valid_palindrome import *

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("Aa", True),
    (" ", True),
    ("", True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_valid_palindrome(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
