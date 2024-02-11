import pytest
from src.n_queens import *

test_cases = [
    (4, [
        [".Q..",
         "...Q",
         "Q...",
         "..Q."],

        ["..Q.",
         "Q...",
         "...Q",
         ".Q.."]
    ]),
    (1, [["Q"]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_n_queens(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
