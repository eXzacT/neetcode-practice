import pytest
from src.sum_two_integers import *

test_cases = [
    ((1, 2), 3),
    ((2, 3), 5),
    ((10, 11), 21),
    ((4, 5), 9),
    ((20, 30), 50),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_sum_two_integers(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
