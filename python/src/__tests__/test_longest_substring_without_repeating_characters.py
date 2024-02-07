import pytest
from src.longest_substring_without_repeating_characters import *

test_cases = [
    ("abcabcbb", 3),
    ("abcabcbdb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    (" ", 1),
    ("dvdf", 3),
    ("", 0),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_longest_substring_without_repeating_characters(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
