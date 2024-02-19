import pytest
from src.edit_distance_levenshtein import *

test_cases = [
    (("horse", "ros"), 3),
    (("intention", "execution"), 5),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_edit_distance_levenshtein(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
