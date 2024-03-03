import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' In this problem, a tree is an undirected graph that is connected and has no cycles.
    You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
    The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
    The graph is represented as an array 'edges' of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
    Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
    If there are multiple answers, return the answer that occurs last in the input.'''


@time_execution()
def sol(edges: list[list[int]]) -> tuple[int, int]:
    n = len(edges)+1
    parent = [i for i in range(n)]
    rank = [1]*n

    def find(n: int) -> int:
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]

        return p

    def union(n1: int, n2: int) -> bool:
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]

        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return (n1, n2)


@time_execution()
def sol_nx(edges: list[list[int]]) -> tuple[int, int]:
    G = nx.Graph()
    for u, v in edges:
        G.add_edge(u, v)
        try:
            nx.find_cycle(G)
            # Found a cycle when we added the edge, return it immediately
            return (u, v)
        except nx.NetworkXNoCycle:
            pass
