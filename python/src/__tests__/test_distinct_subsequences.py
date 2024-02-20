import pytest
from src.distinct_subsequences import *

test_cases = [
    (("rabbbit", "rabbit"), 3),
    (("babgbag", "bag"), 5),
    (("b", "a"), 0),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_distinct_subsequences(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
