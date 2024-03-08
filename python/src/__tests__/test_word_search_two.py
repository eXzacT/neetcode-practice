import pytest
from src.word_search_two import *

test_cases = [
    (([
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ], ["oath", "pea", "eat", "rain"]), ["oath", "eat"]),
    (([
        ["a", "b"],
        ["c", "d"]
    ], ["abcb"]), []),
    (([["a"]], ["a"]), ["a"]),
    (([["a"]], ["b"]), []),
    (([["a", "a"]], ["aaa"]), []),
    (([
        ["a", "b", "c", "e"],
        ["x", "x", "c", "d"],
        ["x", "x", "b", "a"]
    ], ["abc", "abcd"]), ["abc", "abcd"]),
    (([
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ], ["oath", "pea", "eat", "rain", "hklf", "hf"]), ["oath", "eat", "hklf", "hf"]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_word_search_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert sorted(func(*test_input)) == sorted(expected)
