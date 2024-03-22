import pytest
from src.meeting_rooms import *

test_cases = [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[0, 8], [8, 10]], True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_meeting_rooms(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
