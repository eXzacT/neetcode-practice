import pytest
from src.longest_common_subsequence import *

test_cases = [
    (("abcde", "ace"), 3),
    (("abc", "abc"), 3),
    (("abc", "def"), 0),
    (("bsbininm", "jmjkbkjkv"), 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_longest_common_subsequence(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
