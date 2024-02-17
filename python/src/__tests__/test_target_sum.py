import pytest
from src.target_sum import *

test_cases = [
    (([1, 1, 1, 1, 1], 3), 5),
    (([1], 1), 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_target_sum(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
