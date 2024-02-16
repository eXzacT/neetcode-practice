import pytest
from src.palindromic_substrings import *

test_cases = [
    ("abc", 3),
    ("aaa", 6),
    ("a", 1),
    ("aba", 4),
    ("abc", 3),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_palindromic_substrings(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
