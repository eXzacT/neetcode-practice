import pytest
from src.house_robber import *

test_cases = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 7, 9, 30, 40, 1, 2, 3, 4, 19, 20, 30, 1, 2, 3, 4], 109),
    ([0], 0),

]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_house_robber(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
