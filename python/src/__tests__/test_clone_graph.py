from src.clone_graph import *

test_cases = [
    ([[2, 4], [1, 3], [2, 4], [1, 3]]),
    ([[]]),
    ([]),
]


def test_clone_graph():
    for tc in test_cases:
        print(f"\nFor input {tc}")

        original = create(tc)

        for func in [clone_graph, clone_graph_iter]:
            deep_copy = func(original)
            assert deep_copy != original \
                or (deep_copy == None and original == None) \
                and display(deep_copy) == display(original)
