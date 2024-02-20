import pytest
from src.longest_increasing_path_matrix import *

test_cases = [
    ([[9, 9, 4],
      [6, 6, 8],
      [2, 1, 1]], 4),  # 1->2->6->9
    ([[3, 4, 5],
      [3, 2, 6],
      [2, 2, 1]], 4),  # 3->4->5->6
    ([[1]], 1),
    ([[1, 2],
      [2, 3]], 3),  # 1->2->3
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_longest_increasing_path_matrix(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
