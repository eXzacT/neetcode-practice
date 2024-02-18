import pytest
from src.best_time_to_buy_sell_stocks_two import *

test_cases = [
    ([1, 2, 3, 0, 2], 3),
    ([1], 0),
    ([2, 1], 0),
    ([8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6], 10),
    ([10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_best_time_to_buy_sell_stocks_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
