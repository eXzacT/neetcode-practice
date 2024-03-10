import pytest
from src.task_scheduler import *

test_cases = [
    ((["A", "A", "A", "B", "B", "B"], 2), 8),
    ((["A", "C", "A", "B", "D", "B"], 1), 6),
    ((["A", "A", "A", "B", "B", "B"], 3), 10),
    ((["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 1), 12),
    ((["A", "A"], 2), 4),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_task_scheduler(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
