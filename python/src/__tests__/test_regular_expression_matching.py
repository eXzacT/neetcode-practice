import pytest
from src.regular_expression_matching import *

test_cases = [
    (("aa", "a"), False),
    (("aa", "a*"), True),
    (("ab", ".*"), True),
    (("aaaa", "a.*"), True),
    (("aaaaaa", ".*a"), True),
    (("aaaaaabcdad", ".*abcdad"), True),
    (("aab", "c*a*b"), True),
    (("ab", ".*c"), False),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_regular_expression_matching(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
