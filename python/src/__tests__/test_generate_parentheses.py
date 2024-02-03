import pytest
from src.generate_parentheses import *

test_cases = [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (1, ["()"]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_generate_parentheses(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
