import pytest
from src.subsets_two import *

test_cases = [
    ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    ([1, 2, 2, 3],
     [[], [1], [1, 2], [1, 2, 2], [1, 2, 2, 3], [1, 2, 3], [1, 3], [2], [2, 2], [2, 2, 3], [2, 3], [3]]),
    ([0], [[], [0]]),
    ([1, 2, 3, 2],
     [[], [1], [1, 2], [1, 2, 2], [1, 2, 2, 3], [1, 2, 3], [1, 3], [2], [2, 2], [2, 2, 3], [2, 3], [3]]),
    ([4, 4, 4, 1, 4],
     [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_subsets_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert sorted(func(test_input)) == expected
