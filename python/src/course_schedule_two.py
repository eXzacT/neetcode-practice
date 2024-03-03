if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' There are a total of 'courses' you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
    If it is impossible to finish all courses, return an empty array.'''


@time_execution()
def sol_topo_dfs(courses: int, prerequisites: list[tuple[int, int]]) -> list:
    if not prerequisites:
        return [i for i in range(courses)]

    G = {i: [] for i in range(courses)}
    for dest, src in prerequisites:
        G[src].append(dest)

    res = []
    visited = set()
    visiting = set()

    def dfs(course):
        if course in visited:  # Skip already processed courses
            return True
        if course in visiting:  # Cycle
            return False

        visiting.add(course)

        for next_course in G[course]:
            if not dfs(next_course):
                return False

        visiting.remove(course)
        visited.add(course)
        res.append(course)
        return True

    for course in range(courses):
        if course not in visited:
            if not dfs(course):
                return []  # Cycle

    return res[::-1]


@time_execution()
def sol_topo_dfs_v2(courses: int, prerequisites: list[tuple[int, int]]) -> list:
    if not prerequisites:
        return [V for V in range(courses)]

    UNVISITED = 0
    VISITED = 1
    VISITING = 2

    G = {V: [] for V in range(courses)}
    for U, V in prerequisites:
        G[V].append(U)

    visiting = {V: UNVISITED for V in G}
    res = []

    def helper(V: int) -> bool:
        if visiting[V] == VISITED:  # Skip already processed courses
            return True
        if visiting[V] == VISITING:  # Cycle
            return False

        visiting[V] = VISITING

        for E in G[V]:
            if not helper(E):
                return False

        visiting[V] = VISITED
        res.append(V)
        return True

    for V in G:
        if not helper(V):
            return []  # Cycle

    return res[::-1]


@time_execution()
def sol_topo_dfs_v3(courses: int, prerequisites: list[tuple[int, int]]) -> list:
    if not prerequisites:
        return [V for V in range(courses)]

    G = {V: [] for V in range(courses)}
    for course, pre in prerequisites:
        G[course].append(pre)

    visited = set()
    visiting = set()
    res = []

    def helper(V: int) -> bool:
        if V in visiting:  # Cycle
            return False
        if V in visited:
            return True

        visiting.add(V)

        for E in G[V]:
            if not helper(E):
                return False

        visiting.remove(V)
        visited.add(V)
        res.append(V)
        return True

    for V in range(courses):
        if not helper(V):
            return []  # Cycle

    return res


@time_execution()
def sol_topo_indegree(courses: int, prerequisites: list[tuple[int, int]]) -> list:
    if not prerequisites:
        return [V for V in range(courses)]

    G = {V: [] for V in range(courses)}
    indegree = {V: 0 for V in range(courses)}
    for U, V in prerequisites:
        G[V].append(U)
        indegree[U] += 1

    # Start from all the verts with an indegree of 0
    stack = [V for V, D in indegree.items() if D == 0]
    res = []
    while stack:
        V = stack.pop()
        res.append(V)

        for E in G[V]:
            indegree[E] -= 1
            if indegree[E] == 0:
                stack.append(E)

    # If the resulting array isn't of same length as there are courses it can't be topo sorted
    return res if len(res) == courses else []
