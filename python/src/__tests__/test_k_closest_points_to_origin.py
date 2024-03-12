import pytest
from src.k_closest_points_to_origin import *

test_cases = [
    (([[1, 3], [-2, 2]], 1), [[-2, 2]]),
    (([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]]),
]

functions = [globals()[name] for name in dir() if 'sol' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_k_closest_points_to_origin(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
