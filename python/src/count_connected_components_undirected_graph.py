if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
    Return the number of connected components in the graph.'''


@time_execution()
def sol(n: int, edges: list[list[int, int]]) -> int:
    G = {V: [] for V in range(n)}
    for U, V in edges:
        G[U].append(V)
        G[V].append(U)

    visited = set()

    def helper(V: int) -> None:
        if V not in visited:
            visited.add(V)
            for E in G[V]:
                helper(E)

    count = 0
    # Every time we see a node that we didn't visit before it means it's part of a different component
    for V in G:
        if V not in visited:
            helper(V)
            count += 1

    return count


@time_execution()
def sol_v2(n: int, edges: list[list[int, int]]) -> int:
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

    # Start off with assumption that none of the nodes are connected, then subtract them 1 by 1 if they weren't merged
    return n-sum(union(n1, n2) for n1, n2 in edges)
