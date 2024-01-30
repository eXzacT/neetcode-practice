import pytest
from itertools import permutations
from src.group_anagrams import *

test_cases = [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    (["aaa", "bbb", "ccc", "c"],
     [["aaa"], ["bbb"], ["ccc"], ["c"]]),
    (["a"],
     [["a"]]),
    ([''.join(perm) for perm in permutations("plushy", 6)],
     [[''.join(perm) for perm in permutations("plushy", 6)]])
]

functions = [globals()[name] for name in dir() if 'group_anagrams' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_group_anagrams(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
