import pytest
from src.longest_repeating_character_replacement import *

test_cases = [
    (("ABAB", 2), 4),
    (("AABABBA", 1), 4),
    (("AACBCAC", 2), 5),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_longest_repeating_character_replacement(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
