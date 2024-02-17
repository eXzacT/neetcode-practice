import pytest
from src.unique_paths import *

test_cases = [
    ((3, 7), 28),
    ((3, 2), 3),
    ((5, 5), 70),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_unique_paths(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
