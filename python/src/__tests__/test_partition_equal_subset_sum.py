import pytest
from src.partition_equal_subset_sum import *

test_cases = [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
    ([1, 2, 5], False),
    ([1, 2, 3, 10, 4, 5, 8, 9, 10, 23, 5], True),
    ([2, 2, 3, 5], False)
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_partition_equal_subset_sum(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
