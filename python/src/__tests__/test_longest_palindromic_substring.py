import pytest
from src.longest_palindromic_substring import *

test_cases = [
    ("babad", "bab"),
    ("cbbd", "bb"),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_longest_palindromic_substring(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
