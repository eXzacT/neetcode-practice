import pytest
from src.surrounded_regions import *

test_cases = [
    ([
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ],
        [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]),

    ([
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "O"],
        ["X", "O", "X", "X"]
    ],
        [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "O"],
        ["X", "O", "X", "X"]
    ]),

    ([["X"]],
     [["X"]]),

    ([
        ["O", "X", "O", "O", "O", "X"],
        ["O", "O", "X", "X", "X", "O"],
        ["X", "X", "X", "X", "X", "O"],
        ["O", "O", "O", "O", "X", "X"],
        ["X", "X", "O", "O", "X", "O"],
        ["O", "O", "X", "X", "X", "X"]
    ],

        [
        ["O", "X", "O", "O", "O", "X"],
        ["O", "O", "X", "X", "X", "O"],
        ["X", "X", "X", "X", "X", "O"],
        ["O", "O", "O", "O", "X", "X"],
        ["X", "X", "O", "O", "X", "O"],
        ["O", "O", "X", "X", "X", "X"]
    ]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("board,expected", test_cases)
def test_surrounded_regions(board, expected):
    print(f"\nFor input {board}")

    for func in functions:

        func(board)
        assert board == expected
