import pytest
from src.decode_ways import *

test_cases = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("0", 0),
    ("10", 1),
    ("27", 1),
    ("2101", 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_decode_ways(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
