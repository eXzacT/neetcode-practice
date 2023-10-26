from colorama import Fore, Style
from binary_trees import *
from meeting import *
from intervals import *

total_passed_tests = 0
total_tests = 0

meetings = [
    {
        "meeting_time": [(0, 30), (5, 10), (15, 20)],
        "needed_rooms": 2
    },
    {
        "meeting_time": [(5, 8), (9, 15)],
        "needed_rooms": 1
    },
    {
        "meeting_time": [(0, 5), (5, 10), (10, 20)],
        "needed_rooms": 1
    },
    {
        "meeting_time": [(0, 5), (5, 10), (9, 20)],
        "needed_rooms": 2
    },
    {
        "meeting_time": [(0, 20), (0, 30), (0, 40), (5, 10), (20, 50), (0, 50)],
        "needed_rooms": 5
    },
    {
        "meeting_time": [(4, 8), (5, 10), (6, 8), (9, 16), (15, 20)],
        "needed_rooms": 3
    }
]

binary_trees = [
    {
        "correct_array_representation": [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
        "implicit_array_representation": [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
        "explicit_array_representation": [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4],
        "diameter": 6,
        "depth": 4,
        "inverse_tree": ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], True),
        "subtree": ([3, 4, None], True),
        "not_subtree": ([3, 4, 4], False),
        "is_balanced": False
    },
    {
        "correct_array_representation":  [1, 2, 4, None, 3, 4],
        "implicit_array_representation": [1, 2, 4, None, 3, 4],
        "explicit_array_representation": [1, 2, 4, None, 3, 4],
        "diameter": 4,
        "depth": 3,
        "inverse_tree": ([1, 4, 2, None, 4, 3], True),
        "subtree": ([2, 3, None], True),
        "not_subtree": ([4, None, 3, 2], False),
        "is_balanced": True
    }
]

intervals_with_new = [
    {
        "intervals": [[1, 3], [6, 9]],
        "new_interval": [2, 5],
        "output": [[1, 5], [6, 9]]
    },
    {
        "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        "new_interval": [4, 8],
        "output": [[1, 2], [3, 10], [12, 16]]
    },
    {
        "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [18, 20]],
        "new_interval": [4, 8],
        "output": [[1, 2], [3, 10], [12, 16], [18, 20]]
    },
    {
        "intervals": [[5, 6], [8, 9], [10, 11]],
        "new_interval": [4, 8],
        "output": [[4, 9], [10, 11]]
    },
    {
        "intervals": [[5, 6], [8, 9], [10, 11]],
        "new_interval": [2, 3],
        "output": [[2, 3], [5, 6], [8, 9], [10, 11]]
    },
    {
        "intervals": [[5, 6], [8, 9], [10, 11]],
        "new_interval": [12, 14],
        "output": [[5, 6], [8, 9], [10, 11], [12, 14]]
    },
    {
        "intervals": [[8, 9], [5, 6], [10, 11]],
        "new_interval": [12, 14],
        "output": [[5, 6], [8, 9], [10, 11], [12, 14]]
    }
]

intervals_without_new = [
    {
        "intervals": [[1, 4], [6, 7], [9, 11], [2, 11]],
        "output": [[1, 11]]
    },
    {
        "intervals": [[1, 4], [3, 5], [4, 7]],
        "output": [[1, 7]]
    },
    {
        "intervals": [[5, 6], [1, 6], [4, 11], [12, 14]],
        "output": [[1, 11], [12, 14]]
    },
    {
        "intervals": [[8, 9], [6, 7], [10, 11]],
        "output": [[6, 7], [8, 9], [10, 11]]
    }
]


def assert_equals(testing, expected_result, result) -> None:
    """ Check if both values are the same and notifies the user"""
    global total_passed_tests
    global total_tests
    passed = expected_result == result
    if passed:
        total_passed_tests += 1
        test_result, color, equality = "Test passed", Fore.GREEN, "=="
    else:
        test_result, color, equality = "Test failed", Fore.RED, "!="

    print(f"Result for ({testing})\nExpected ({expected_result}) {equality} Got ({result}) " +
          color + test_result + Style.RESET_ALL+"\n")
    total_tests += 1


def print_FAIL(text: str) -> None:
    """ Print test failure 2023-10-24 14:00:43 """
    global total_tests
    total_tests += 1
    print(text + Fore.RED + "\nTest failed" + Style.RESET_ALL+"\n")


def test_meeting():
    for meeting in meetings:

        expected_result = meeting['needed_rooms']
        result = rooms_needed(list(meeting['meeting_time']))

        assert_equals(meeting['meeting_time'], expected_result, result)


def test_binary_trees():
    """ Runs all tests for binary trees 2023-10-25 13:40:24 """

    # TODO Separate tests 2023-10-25 13:40:36
    for tree in binary_trees:

        print("Testing if all 3 initialization functions initialize the same way and if it matches the true representation.")
        tree1 = init_tree(
            tree['implicit_array_representation'], 'implicit_input_iteratively')
        tree2 = init_tree(
            tree['explicit_array_representation'], 'implicit_input_recursively')
        tree3 = init_tree(
            tree['explicit_array_representation'], 'explicit_input')

        result1 = tree_to_array(tree1)
        result2 = tree_to_array(tree2)
        result3 = tree_to_array(tree3)

        # print(result1)
        # print(result2)
        # print(result3)

        # If all three trees are the same then compare it to the true result
        if result1 == result2 == result3:
            assert_equals(tree['correct_array_representation'], result1)
        else:
            print_FAIL(
                "Trees are not initialized the same way so testing needs to be stopped!")
            break

        # "diameter": 6
        print("Testing if diameter returns correct value.")
        assert_equals(tree['diameter'], diameter(tree1))

        # "depth": 4
        print("Testing if depth works as it should.")
        assert_equals(tree['depth'], depth(tree1))

        print("Testing if the inverse works as it should.")
        inverted_tree = invert_tree(tree1)
        result = tree_to_array(inverted_tree)
        expected_result = tree['inverse_tree'][0]
        # "inverse_tree": ([1, 2, 2, 3, None, None, 3, 4, None,None, 4], True)
        # boolean says if this(the inverse) is the same as the original tree
        are_same_trees = result == expected_result
        assert_equals(tree['inverse_tree'][1], are_same_trees)

        print("Testing if both iterative and recursive is_subtree checks work the same way and if they work as they should.")
        # "subtree": ([3,4,None], True)
        subtree = init_implicit_tree_iteratively(tree['subtree'][0])
        iterative_result = is_subtree_iteratively(subtree, tree1)
        recursive_result = is_subtree_recursively(subtree, tree1)
        expected_result = tree['subtree'][1]
        if iterative_result == recursive_result:
            assert_equals(expected_result, iterative_result)
        else:
            print_FAIL(
                "Iterative and Recursive approach to is_subtree results differ!")

        print("Testing if both iterative and recursive is_subtree checks work the same way and if tree is not a subtree.")
        # "not_subtree": ([3,4,4], False)
        subtree = init_implicit_tree_iteratively(tree['not_subtree'][0])
        iterative_result = is_subtree_iteratively(subtree, tree1)
        recursive_result = is_subtree_recursively(subtree, tree1)
        expected_result = tree['not_subtree'][1]
        if iterative_result == recursive_result:
            assert_equals(expected_result, iterative_result)
        else:
            print_FAIL(
                "Iterative and Recursive approach to is_subtree results differ for not_subtree!")

        # "is_balanced": False
        print("Testing if is_balanced works as it should.")
        assert_equals(tree['is_balanced'], is_balanced(tree1))


def test_intervals(intervals, func, has_new_interval=True):
    """ Runs all the tests for intervals """
    for interval in intervals:
        if has_new_interval:
            test = str(interval["intervals"])+" New interval " + \
                str(interval["new_interval"])
            result = func(interval['intervals'], interval['new_interval'])
        else:
            test = str(interval["intervals"])
            result = func(interval["intervals"])
        expected_result = interval['output']
        assert_equals(test, expected_result, result)


# run all the tests
# test_meeting()
# test_binary_trees()
test_intervals(intervals_with_new, insert_into_intervals)
test_intervals(intervals_without_new, merge_intervals, has_new_interval=False)

print(f"Total tests ran: {total_tests}\n"
      + Fore.GREEN
      + f"Passed: {total_passed_tests}\n"
      + (Fore.RED + f"Failed: {total_tests - total_passed_tests} " if total_tests -
         total_passed_tests > 0 else "")
      + Style.RESET_ALL
      + "\n")

# visualize_binary_tree(init_implicit_tree_iteratively([1,2,2,3,None,None,3,4,None,None,4]))
