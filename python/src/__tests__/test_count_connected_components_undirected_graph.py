import pytest
from src.count_connected_components_undirected_graph import *

test_cases = [
    ((5, [[0, 1], [1, 2], [3, 4]]), 2),
    ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_count_connected_components_undirected_graph(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
