import pytest
from src.best_time_to_buy_sell_stocks import *

test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([9, 2, 5, 8, 3, 7, 10, 1, 11, 2, 4], 10),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_best_time_to_buy_sell_stocks(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
