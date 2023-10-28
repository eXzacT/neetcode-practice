from test_data import binary_trees
from binary_trees import *


def test_binary_trees_initialization():
    """ Check if all array representation of the tree gets initialized the same way (28/10/2023) """

    for tree in binary_trees:
        expected_tree_array = tree["implicit_representation"]

        tree1 = init_tree(tree["implicit_representation"],
                          method='implicit_iteratively')
        tree2 = init_tree(tree["explicit_representation"],
                          method='explicit_iteratively')
        tree3 = init_tree(tree["explicit_representation"],
                          method='explicit_recursively')

        tree1 = tree_to_array(tree1)
        tree2 = tree_to_array(tree2)
        tree3 = tree_to_array(tree3)

        # If all 3 trees were initialized the same way then check if they're the same as the expected (28/10/2023)
        if (tree1 == tree2 == tree3):
            assert tree1 == expected_tree_array, f"Tree {tree1} is different from the expected tree: {expected_tree_array}"

        else:
            AssertionError("Trees are not initialized the same way.")


def test_diameter_returns_correct_value():

    for tree in binary_trees:
        expected_diameter = tree["diameter"]
        tree_array = tree["explicit_representation"]

        tree = init_tree(tree_array, 'explicit_recursively')

        assert diameter(
            tree) == expected_diameter, f"Diameter is not calculated correctly for :{tree_array}"


def test_depth_returns_correct_value():

    for tree in binary_trees:
        expected_depth = tree["depth"]
        tree_array = tree["explicit_representation"]

        tree = init_tree(tree_array, 'explicit_recursively')

        assert depth(
            tree) == expected_depth, f"Depth is not calculated correctly for :{tree_array}"


def test_inverse_returns_correct_value():

    for tree in binary_trees:
        expected_inverse = tree["inverse_tree"]
        tree_array = tree["explicit_representation"]

        tree = init_tree(tree_array, 'explicit_recursively')
        reversed_tree = invert_tree(tree)

        assert tree_to_array(
            reversed_tree) == expected_inverse, f"Inverse is not calculated correctly for :{tree_array}"


def test_tree_is_a_subtree_of_a_tree():

    for tree in binary_trees:
        subtree_array = tree["subtree"]
        tree_array = tree["implicit_representation"]

        tree = init_tree(tree_array, 'implicit_iteratively')
        subtree = init_tree(subtree_array, 'implicit_iteratively')
        res_recursive = is_subtree_iteratively(subtree, tree)
        res_iterative = is_subtree_recursively(subtree, tree)

        assert True == res_recursive == res_iterative, f"{tree_array} fails {subtree_array} subtree check"


def test_tree_is_not_a_subtree_of_a_tree():

    for tree in binary_trees:
        not_subtree_array = tree["not_subtree"]
        tree_array = tree["implicit_representation"]

        tree = init_tree(tree_array, 'implicit_iteratively')
        subtree = init_tree(not_subtree_array, 'implicit_iteratively')
        res_recursive = is_subtree_iteratively(subtree, tree)
        res_iterative = is_subtree_recursively(subtree, tree)

        assert False == res_recursive == res_iterative, f"{tree_array} fails {not_subtree_array} subtree check"


def test_tree_is_balanced_returns_correct_value():

    for tree in binary_trees:
        expected_balance = tree["is_balanced"]
        tree_array = tree["implicit_representation"]

        tree = init_tree(tree_array, 'implicit_iteratively')

        assert is_balanced(
            tree) == expected_balance, f"{tree_array} fails balanced check"


def test_are_same_returns_correct_value():

    for tree in binary_trees:

        tree_array = tree["implicit_representation"]
        tree = init_tree(tree_array, 'implicit_iteratively')

        assert are_same_iteratively(tree, tree) == are_same_recursively(
            tree, tree), f"{tree_array} fails same check"
