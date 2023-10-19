from collections import deque
import time
class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

#iteratively
def init_tree(array)->TreeNode:
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

#recursively
def init_tree(array,index=0)->TreeNode:
    if array is None:
        return None
    if index>=len(array) or array[index] is None:
        return None
    root=TreeNode(array[index])
    root.left=init_tree(array,2*index+1)
    root.right=init_tree(array,2*index+2)
    
    return root

def print_tree(tree:TreeNode):
    if tree is None:
        return None
    queue=deque([tree])
    while queue:
        root=queue.popleft()
        print(root.value)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

def depth(tree:TreeNode):
    if tree is None:
        return 0
    return 1+(max(depth(tree.left),depth(tree.right)))

def diameter(tree:TreeNode)->int:
    timer_start=time.time()
    if tree is None:
        return None
    max_left=max_right=0
    if tree.left:
        max_left=depth(tree.left)
    if tree.right:
        max_right=depth(tree.right)
    timer_end=time.time()
    total_time=timer_end-timer_start
    return max_left+max_right,total_time

def diameter2(root)->int:
    timer_start=time.time()
    max_diameter = [0]  # Using a list here so it's passed by reference

    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        return max(left_height, right_height) + 1

    height(root)
    timer_end=time.time()
    total_time=timer_end-timer_start
    return max_diameter[0],total_time

def isBalanced(tree:TreeNode)->bool:
    if tree is None:
        return None
    if (depth(tree.left)-depth(tree.right)) not in [-1,0,1]:
        return False
        
    return True

array1=[]
for i in range(0,500_000):
    array1.append(i)

array=[1,2,3,None,None,3,None,None,None,None,None,11]

tree=init_tree(array)
print_tree(tree)
print("Tree is"+(" not" if not isBalanced(tree) else "")+" balanced")
print("Depth of this tree is",depth(tree))
print("Diameter of this tree is",diameter2(tree))
print("Diameter of this tree is",diameter(tree))