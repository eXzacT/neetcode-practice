import pytest
from src.permutation_in_string import *

test_cases = [
    (("ab", "eidbaooo"), True),
    (("ab", "eidboaoo"), False),
    (("abcdxabcde", "abcdeabcdx"), True),
    (("rmqqh", "nrsqrqhrymf"), False),
    (("rmqqhsdasdadsadsds", "nrsqrqhrymf"), False),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_permutation_in_string(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
