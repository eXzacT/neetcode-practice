import pytest
from src.minimum_window_substring import *

test_cases = [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"), "a"),
    (("a", "aa"), ""),
    (("ABFBD", "BAD"), "ABFBD"),
    (("bba", "ab"), "ba"),
    (("bbaa", "aba"), "baa"),
    (("aa", "aa"), "aa"),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_minimum_window_substring(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
