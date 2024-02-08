import pytest
from src.subsets import *

test_cases = [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([0], [[], [0]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_subsets(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        # Sorted because different approaches are giving different order
        assert sorted(func(test_input)) == sorted(expected)
