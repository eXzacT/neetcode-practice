import pytest
from src.ways_to_climb import *

test_cases = [
    (1, 1),
    (2, 2),
    (3, 3),
    (10, 89),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_ways_to_climb(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
