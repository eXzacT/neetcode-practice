import pytest
from src.house_robber_two import *

test_cases = [
    ([2, 3, 2], 3),
    ([0, 0], 0),
    ([0, 2], 2),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([2, 2, 3, 4], 6),
    ([1, 3, 1, 3, 100], 103),
    ([3], 3),
    ([0], 0),
    ([200, 3, 140, 20, 10], 340),
    ([4, 1, 2, 7, 5, 3, 1], 14),
    ([2, 1, 1, 2], 3),
    ([2, 2, 4, 3, 2, 5], 10),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_house_robber_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
