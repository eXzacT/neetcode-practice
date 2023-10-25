from collections import deque
import graphviz


class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None


def init_tree(array: list, method: str) -> TreeNode:
    match method:
        case 'implicit_input_iteratively':
            root = init_implicit_tree_iteratively(array)
        case 'implicit_input_recursively':
            root = init_implicit_tree_recursively(array)
        case 'explicit_input':
            root = init_explicit_tree_iteratively(array)
        case _:
            raise ValueError("Invalid method")

    return root

# Works for arrays of type array = [1, 2, 2, 3, None, None, 3, 4, None,None, 4]


def init_implicit_tree_iteratively(array) -> TreeNode:
    """ Initiates binary tree iteratively """
    if array is None:
        return None
    root = TreeNode(array[0])
    queue = deque([root])
    index = 1
    while queue and index < len(array):
        node = queue.popleft()
        if (array[index] is not None):
            node.left = TreeNode(array[index])
            queue.append(node.left)
        index += 1
        if (index < len(array) and array[index] is not None):
            node.right = TreeNode(array[index])
            queue.append(node.right)
        index += 1

    return root

# Works for arrays of type array = [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4]
# but not for type array = [1, 2, 2, 3, None, None, 3, 4, None,None, 4]


def init_explicit_tree_iteratively(array) -> TreeNode:
    """ Initiates binary tree iteratively """
    def attach_node(parent, child_value, position):
        if child_value is not None:
            child = TreeNode(child_value)
            if position == 'left':
                parent.left = child
            else:
                parent.right = child
            return child
        return None

    if not array:
        return None
    root = TreeNode(array[0])
    queue = deque([root])
    index = 1
    while index < len(array):
        node = queue.popleft()

        # Handling left child
        left_child = attach_node(node, array[index], 'left')
        queue.append(left_child or None)
        index += 1

        # Handling right child
        if index < len(array):
            right_child = attach_node(node, array[index], 'right')
            queue.append(right_child or None)
            index += 1

    return root

# Works for arrays of type array = [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4]


def init_implicit_tree_recursively(array, index=0) -> TreeNode:
    """ Initiates binary tree recursively """
    if index >= len(array) or array[index] is None:
        return None
    root = TreeNode(array[index])
    root.left = init_implicit_tree_recursively(array, 2*index+1)
    root.right = init_implicit_tree_recursively(array, 2*index+2)

    return root


def invert_tree(root: TreeNode) -> TreeNode:
    """ Inverts binary tree recursively """
    if root is None:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    invert_tree(root.left)
    invert_tree(root.right)

    return root


def depth(root: TreeNode) -> int:
    """ Calculates max depth(height) of the tree """
    if root is None:
        return 0
    return 1+(max(depth(root.left), depth(root.right)))


def print_tree(root: TreeNode) -> None:
    """ Print the tree in a visual way """
    if root is None:
        return None

    max_depth = depth(root)

    # Now we print the tree level by level
    level = 0
    queue = deque([(root, level)])
    output = [""] * max_depth

    while queue:
        node, level = queue.popleft()
        # Adjust the calculation of spaces here
        spaces = " " * (2 ** (max_depth - level) - 1)
        output[level] += spaces
        if node is None:
            output[level] += " "
            spaces += " "
        else:
            output[level] += str(node.value)
        output[level] += spaces

        if level + 1 < max_depth:
            queue.append((node.left if node else None, level + 1))
            queue.append((node.right if node else None, level + 1))

    # Finally, we print each level of the output
    for line in output:
        print(line)


def tree_to_array(root: TreeNode) -> list:
    """ Transforms a binary tree into an array representation 2023-10-25 13:15:17 """
    if not root:
        return []

    queue = deque([root])
    array = []

    while queue:
        node = queue.popleft()

        # If the node is None, append None to array and continue
        if node is None:
            array.append(None)
            continue

        # If the node is not None, append its value to array
        array.append(node.value)

        # For both left and right children, if they exist append them to the queue,
        # otherwise, append a None value to represent a missing child.
        queue.append(node.left if node.left else None)
        queue.append(node.right if node.right else None)

    # Remove trailing None values from the array
    while array and array[-1] is None:
        array.pop()

    return array


def visualize_binary_tree(root: TreeNode) -> None:
    """ Generate a png image of a tree 2023-10-25 13:14:57 """
    if root is None:
        print("The tree is empty.")
        return

    dot = graphviz.Digraph(graph_attr={'size': '100,100!'})
    dot.node(str(id(root)), str(root.value))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(id(node.left)), str(node.left.value))
            dot.edge(str(id(node)), str(id(node.left)))
            add_nodes_edges(node.left)
        if not node.left and node.right:  # Add a "None" node when the node has a right child but no left child
            null_node_id = id(node) * 2
            dot.node(str(null_node_id), 'None')
            dot.edge(str(id(node)), str(null_node_id))

        if node.right:
            dot.node(str(id(node.right)), str(node.right.value))
            dot.edge(str(id(node)), str(id(node.right)))
            add_nodes_edges(node.right)
        if node.left and not node.right:  # Add a "None" node when the node has a left child but no right child
            null_node_id = id(node) * 2 + 1
            dot.node(str(null_node_id), 'None')
            dot.edge(str(id(node)), str(null_node_id))

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')


def diameter(root: TreeNode) -> int:
    """ Calculate the max diameter of a tree 2023-10-25 13:15:58 """
    # Using a list because it's mutable(height can manipulate its contents and keep them)
    max_diameter = [0]

    # Helper function which gets max height of a tree, we are also changing max diameter inside it, which equals to
    # Maximum left+right height
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        return max(left_height, right_height) + 1

    height(root)
    return max_diameter[0]


def is_balanced(root: TreeNode) -> bool:
    """ If the difference in heights of each LEFT and RIGHT subtree is not more than 1 2023-10-25 13:16:29 """
    def dfs(root):
        if not root:
            return [True, 0]
        left, right = dfs(root.left), dfs(root.right)
        balanced = (left[0] and right[0] and
                    abs(left[1]-right[1]) <= 1)
        return [balanced, 1+max(left[1], right[1])]
    return dfs(root)[0]


def are_same_recursively(root1: TreeNode, root2: TreeNode) -> bool:
    """ Check if structure of both trees and values are the same 2023-10-25 13:17:25 """

    # make sure the nodes are equal if one of them is None(so they are both None)
    if root1 is None or root2 is None:
        return root1 == root2
    return root1.value == root2.value and are_same_recursively(root1.left, root2.left) and are_same_recursively(root1.right, root2.right)


def are_same_iteratively(root1: TreeNode, root2: TreeNode) -> bool:
    """ Iterative version of the above function 2023-10-25 13:17:54 """
    queue = deque([(root1, root2)])
    while queue:
        root1, root2 = queue.popleft()

        # If either root2 or root1 is None, then both should be None
        if not root2 or not root1:
            if root1 != root2:
                return False
            continue

        if root1.value != root2.value:
            return False

        queue.append([root1.left, root2.left])
        queue.append([root1.right, root2.right])

    return True


def is_subtree_recursively(sub_tree: TreeNode, main_tree: TreeNode) -> bool:
    """ Checks if a tree is a subtree of another tree 2023-10-25 13:18:08 """
    if not main_tree:
        return False
    if not sub_tree:
        return True

    # First check both full trees then check left and right subtrees
    return are_same_recursively(main_tree, sub_tree) or is_subtree_recursively(sub_tree, main_tree.left) or is_subtree_recursively(sub_tree, main_tree.right)


def is_subtree_iteratively(sub_tree: TreeNode, main_tree: TreeNode) -> bool:
    """ Iterative version of the above function 2023-10-25 13:18:26 """
    if not sub_tree:
        return True
    if not main_tree:
        return False

    queue = deque([main_tree])

    while queue:
        current_node = queue.popleft()

        if current_node is not None and current_node.value == sub_tree.value:
            return are_same_iteratively(current_node, sub_tree)

        # Otherwise, continue with the traversal of main_tree, we will compare the children to sub_tree root next run
        if current_node:
            queue.append(current_node.left)
            queue.append(current_node.right)

    return False
