import pytest
from src.contains_duplicate import *

test_cases = [
    ([1, 3, 4, 6, 9, 0], False),
    ([1, 4, 5, 6, 8, 9, 1], True),
    ([num for num in range(1000)]+[900], True)
]

functions = [globals()[name] for name in dir() if 'contains_duplicate' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_contains_duplicate(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
