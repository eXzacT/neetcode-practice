import pytest
from src.pacific_atlantic_water_flow import *

test_cases = [
    ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [
     5, 1, 1, 2, 4]], [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]),
    ([[1]], [(0, 0)]),
    ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [
     (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]),
    ([[10, 10, 10], [10, 1, 10], [10, 10, 10]], [
     (0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_pacific_atlantic_water_flow(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
