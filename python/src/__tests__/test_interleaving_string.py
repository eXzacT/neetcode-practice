import pytest
from src.interleaving_string import *

test_cases = [
    (("aabcc", "dbbca", "aadbbcbcac"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (("abc", "cdefg", "abcdefgc"), True),
    (("", "", ""), True),
    (("aaaa", "aa", "aaa"), False),
    (("a", "", "c"), False),
    (("a", "b", "ab"), True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_interleaving_string(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
