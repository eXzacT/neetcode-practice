import pytest
from src.power_x_to_n import *

test_cases = [
    ((2.00000, 10), 1024.00000),
    ((2.10000, 3), 9.26100),
    ((2.00000, -2), 0.25000),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_power_x_to_n(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
