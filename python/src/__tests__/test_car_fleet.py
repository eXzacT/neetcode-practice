import pytest
from src.car_fleet import *

test_cases = [
    ((12,  [10, 8, 0, 5, 3],  [2, 4, 1, 1, 3]), 3),
    ((10,  [3],  [3]), 1),
    ((100,  [0, 2, 4],  [4, 2, 1]), 1),
    ((10,  [6, 8],  [3, 2]), 2),
    ((10,  [0, 4, 2],  [2, 1, 3]), 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_car_fleet(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
