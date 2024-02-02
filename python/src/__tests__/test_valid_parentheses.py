import pytest
from src.valid_parentheses import *

test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("{[]}", True),
    ("{[", False),
    ("{", False),
    ("]", False),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_valid_parentheses(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
