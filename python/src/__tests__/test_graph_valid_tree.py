import pytest
from src.graph_valid_tree import *

test_cases = [
    ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
    ((4, [[0, 1], [0, 2], [0, 3], [1, 2]]), False),
    ((3, [[0, 1], [1, 2]]), True),
    ((3, [[0, 1], [1, 2], [2, 0]]), False),
    ((1, []), True),
    ((2, [[0, 1]]), True),
    ((2, [[0, 1], [1, 0]]), False),
    ((5, [[0, 1], [1, 4], [0, 2]]), False),
    ((4, [[0, 1], [1, 2], [2, 3], [3, 0]]), False),
    ((6, [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5]]), False),
]


functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_graph_valid_tree(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
