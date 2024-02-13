import pytest
from src.ways_to_climb import *

# Only allowed to jump 1 or 2 steps
test_cases = [
    (1, 1),
    (2, 2),
    (3, 3),
    (10, 89),
]

functions_ways = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_ways_to_climb_one_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions_ways:
        assert func(test_input) == expected


# Allowed to jump any length from a given array
test_cases_2 = [
    ((10, [2, 4, 5, 8]), 11),
]


functions_ways_multiple = [
    ways_to_climb_dp, ways_to_climb_memo, ways_to_climb_rec, ways_to_climb_nx]


@pytest.mark.parametrize("test_input,expected", test_cases_2)
def test_ways_to_climb_multiple(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions_ways_multiple:
        assert func(*test_input) == expected
