if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given n nodes labeled from 0 to n-1 and a list of undirected edges, write a function to check whether these edges make a valid tree'''


@time_execution()
def sol_dfs(n: int, edges: list[list[int, int]]) -> bool:
    G = {V: [] for V in range(n)}
    for U, V in edges:
        G[U].append(V)
        G[V].append(U)

    if len(G) != n:
        return False
    visiting = set()
    visited = set()

    def cyclic(curr: int) -> bool:
        if curr in visited:
            return True
        if curr in visiting:
            return False

        visiting.add(curr)
        for E in G[curr]:
            if cyclic(E):
                return True

        visited.add(curr)
        visiting.remove(curr)
        return False

    # No loop and visited the entire graph = tree
    return not cyclic(0) and len(visited) == n


@time_execution()
def sol_dfs_v2(n: int, edges: list[list[int, int]]) -> bool:
    G = {V: [] for V in range(n)}
    for U, V in edges:
        G[U].append(V)
        G[V].append(U)

    if len(G) != n:
        return False
    visited = set()

    def cyclic(curr: int, prev: int) -> bool:
        if curr in visited:
            return True

        visited.add(curr)
        for E in G[curr]:
            # Don't go back(it's undirected so verts are connected bothways)
            if E == prev:
                continue
            if cyclic(E, curr):
                return True

        return False

    # No loop and visited the entire graph = tree
    return not cyclic(0, -1) and len(visited) == n


@time_execution()
def sol_v3(n: int, edges: list[list[int, int]]) -> bool:
    G = {V: [] for V in range(n)}
    for U, V in edges:
        G[U].append(V)
        G[V].append(U)

    # Visit all nodes that can possibly be visited
    def dfs(V: int):
        if V not in visited:
            visited.add(V)
            for E in G[V]:
                dfs(E)

    visited = set()
    dfs(0)

    # Fully connected and acyclic = tree
    return len(visited) == n and len(edges)*2 == 2*(len(G)-1)
