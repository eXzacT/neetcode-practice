from collections import defaultdict
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.'''


class Node:
    def __init__(self, val=0, neighbours=None):
        self.val = val
        self.neighbours = neighbours if neighbours else []


def create(adj_list: list[list[int]]) -> Node:
    if not adj_list:
        return None

    nodes = {}
    for curr_val, adjs in enumerate(adj_list, start=1):
        if curr_val not in nodes:
            nodes[curr_val] = Node(curr_val)
        for adj_val in adjs:
            if adj_val not in nodes:
                nodes[adj_val] = Node(adj_val)
            nodes[curr_val].neighbours.append(nodes[adj_val])

    return nodes[1]


def display(node: Node) -> list[list[int]]:
    if not node:
        return []

    adj_dict = defaultdict(list)
    visited = set()

    def dfs(curr):
        if curr.val in visited:
            return
        visited.add(curr.val)
        for neighbour in curr.neighbours:
            if neighbour.val not in adj_dict[curr.val]:
                adj_dict[curr.val].append(neighbour.val)
            dfs(neighbour)

    dfs(node)
    return [adj_dict[i] for i in sorted(adj_dict)]


@time_execution()
def clone_graph(node: Node) -> Node:
    nodes_dict = {}

    def dfs(curr: Node) -> Node:
        if curr in nodes_dict:
            return nodes_dict[curr]

        copy = Node(curr.val)
        nodes_dict[curr] = copy
        for n in curr.neighbours:
            copy.neighbours.append(dfs(n))

        return copy

    return dfs(node) if node else None


@time_execution()
def clone_graph_iter(node: Node) -> Node:
    if not node:
        return None

    # A dictionary to keep track of copied nodes
    nodes_dict = {node: Node(node.val)}
    stack = [node]

    while stack:
        curr = stack.pop()

        for n in curr.neighbours:
            # If this neighbor hasn't been copied yet
            if n not in nodes_dict:
                nodes_dict[n] = Node(n.val)
                stack.append(n)

            # Add this neighbor to the current node's copy
            nodes_dict[curr].neighbours.append(nodes_dict[n])

    # Return the copy of the input node
    return nodes_dict[node]
