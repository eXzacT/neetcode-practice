import pytest
from src.keypad_letter_combinations import *

test_cases = [
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("2", ["a", "b", "c"]),
    ("", []),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_keypad_letter_combinations(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
