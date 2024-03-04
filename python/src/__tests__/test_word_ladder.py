import pytest
from src.word_ladder import *

test_cases = [
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    (("a", "c", ["a", "b", "c"]), 2),
    (("hot", "dog", ["hot", "dog", "dot"]), 3)
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_word_ladder(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
