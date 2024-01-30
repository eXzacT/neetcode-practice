import pytest
from src.valid_anagram import *

test_cases = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("aaac", "ac"), False),
    (("aaac", "acac"), False),
]

functions = [globals()[name] for name in dir() if 'valid_anagram' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_valid_anagram(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
