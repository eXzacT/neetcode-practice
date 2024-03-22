import pytest
from src.meeting_rooms_two import *

test_cases = [
    ([[0, 30], [5, 10], [15, 20]], 2),
    ([[7, 10], [2, 4]], 1),
    ([[1, 5], [8, 9], [8, 10]], 2),
    ([[6, 10], [1, 3], [2, 4], [3, 7]], 2),
    ([[1, 3], [2, 6], [8, 10], [9, 11]], 2),
    ([[0, 30], [5, 10], [15, 20], [17, 25]], 3),
    ([[1, 4], [5, 6], [8, 9], [2, 6]], 2),
    ([[4, 9], [4, 17], [9, 10]], 2),
    ([[2, 11], [6, 16], [11, 16]], 2),
    ([[1, 8], [6, 20], [9, 16], [4, 8]], 3),
    ([[3, 10], [2, 6], [1, 3], [6, 9]], 2)
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_meeting_rooms_two(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
