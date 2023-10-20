from collections import deque
import graphviz

class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

#iteratively
#like array = [1, 2, 2, 3, None, None, 3, 4, None,None, 4]
def init_tree_iteratively(array)->TreeNode:
    if array is None:
        return None
    root=TreeNode(array[0])
    queue=deque([root])
    index=1
    while queue and index<len(array):
        node=queue.popleft()
        if(array[index] is not None):
            node.left=TreeNode(array[index])
            queue.append(node.left)
        index+=1
        if(index<len(array) and array[index] is not None):
            node.right=TreeNode(array[index])
            queue.append(node.right)
        index+=1

    return root

#iteratively
#like array = [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4]
def init_tree_iteratively_with_placeholders(array)->TreeNode:
    if not array:
        return None
    root = TreeNode(array[0])
    queue = deque([root])
    index = 1
    while index < len(array):
        node = queue.popleft()
        
        # Handling left child
        if array[index] is not None:
            left_child = TreeNode(array[index])
            if node:  # Only attach if the current parent node exists
                node.left = left_child
            queue.append(left_child)
        else:
            queue.append(None)
        index += 1
        
        # Handling right child
        if index < len(array):
            if array[index] is not None:
                right_child = TreeNode(array[index])
                if node:  # Only attach if the current parent node exists
                    node.right = right_child
                queue.append(right_child)
            else:
                queue.append(None)
            index += 1

    return root

#recursively
#like array = [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4]
def init_tree_recursively(array,index=0)->TreeNode:
    if index >= len(array) or array[index] is None:
        return None
    root=TreeNode(array[index])
    root.left = init_tree_recursively(array, 2*index+1)
    root.right = init_tree_recursively(array, 2*index+2)
    
    return root

def invert_tree(root:TreeNode)->TreeNode:
    if root is None:
        return None
    
    temp=root.left
    root.left=root.right
    root.right=temp

    invert_tree(root.left)
    invert_tree(root.right)

    return root

#calculate max depth of the tree
def depth(root:TreeNode):
    if root is None:
        return 0
    return 1+(max(depth(root.left),depth(root.right)))

#print the tree in a visual way
def print_tree(root:TreeNode):
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

""" def print_tree(root:TreeNode):
    if root is None:
        return None
    queue=deque([root])
    while queue:
        node=queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) """

#generate a png image of a tree
def visualize_binary_tree(root):
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

def diameter(root)->int:
    max_diameter = [0]  # Using a list here so it's passed by reference

    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        return max(left_height, right_height) + 1

    height(root)
    return max_diameter[0]

def isBalanced(root:TreeNode)->bool:
    def dfs(root):
        if not root:return [True,0]
        left,right=dfs(root.left),dfs(root.right)
        balanced=(left[0] and right[0] and 
                  abs(left[1]-right[1])<=1)
        return [balanced,1+max(left[1],right[1])]
    return dfs(root)[0]

def areSame(root1:TreeNode,root2:TreeNode)->bool:
    if root1 is None or root2 is None:
        return root1==root2
    return root1.value==root2.value and areSame(root1.left,root2.left) and areSame(root1.right,root2.right)

array=[1,2,2,3,None,None,3,4,None,None,500]
array=[5, 3, 7, 2, None, 2, 8,9,10,11,123]
array=[5, 3, 7, 1, 4, None, 8,2,None,3,4,2,2,3,4]
array = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
array = [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4]

tree=init_tree_iteratively_with_placeholders(array)
print_tree(tree)
tree=init_tree_recursively(array)
print_tree(tree)
array = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
tree1=init_tree_iteratively(array)
print_tree(tree1)
tree2=invert_tree(tree)
print_tree(tree2)

print("Trees are"+
      (" not" if not  areSame(tree1,tree2) else "")
      +" the same")
   
print("Tree is"+
      (" not" if not isBalanced(tree) else "")
      +" balanced")
print("Diameter of this tree using diameter2 function is",diameter(tree))
print("Depth of this tree is",depth(tree))
#visualize_binary_tree(tree)