import pytest
from src.codec import *

test_cases = [
    (["lint", "code", "love", "you"], ["lint", "code", "love", "you"]),
    (["#dog", "og#g", "hash#", "ha#sh"], ["#dog", "og#g", "hash#", "ha#sh"]),
    (["#3dog", "og3#g", "ha3sh#", "ha3#sh"],
     ["#3dog", "og3#g", "ha3sh#", "ha3#sh"]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_codec(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
