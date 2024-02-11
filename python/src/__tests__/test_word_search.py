import pytest
from src.word_search import *

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

board2 = [
    ["W", "B", "B", "W"],
    ["A", "B", "B", "A"],
    ["S", "F", "C", "S"],
    ["A", "B", "B", "A"],
    ["W", "B", "B", "W"],
]

board3 = [
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]
]

board4 = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"]
]

test_cases = [
    ((board, "ABCCED"), True),
    ((board, "SEE"), True),
    ((board, "ABCB"), False),
    ((board2, "WASABI"), False),
    ((board3, "AAB"), True),
    ((board4, "ABCESEEEFS"), True),
    (([["a"]], "a"), True),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_word_search(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
