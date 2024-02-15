import pytest
from src.construct_can import *

test_cases = [
    (("leetcode", ["leet", "code"]), True),
    (("applepenapple", ["apple", "pen"]), True),
    (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
    (("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]), True),
    (("cars", ["car", "ca", "rs"]), True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_construct_can(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
