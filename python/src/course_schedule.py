from collections import defaultdict
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.'''


@time_execution()
def sol_dfs(courses: int, prerequisites: list[list[int]]) -> bool:
    prev_map = {i: [] for i in range(courses)}
    for p, q in prerequisites:
        prev_map[p].append(q)

    visiting = set()

    def dfs(curr: int) -> bool:
        if curr in visiting:  # Cycle
            return False
        if not prev_map[curr]:
            return True

        visiting.add(curr)
        for prev in prev_map[curr]:
            if not dfs(prev):
                return False

        visiting.remove(curr)
        prev_map[curr] = []
        return True

    return all(dfs(i) for i in range(courses))


@time_execution()
def sol_dfs_v2(courses: int, prerequisites: list[list[int]]) -> bool:
    prev_map = {i: set() for i in range(courses)}
    for p, q in prerequisites:
        if p in prev_map[q] or p == q:  # Cycle between 2 courses or self cycle
            return False
        prev_map[p].add(q)

    visiting = set()

    def dfs(curr: int) -> bool:
        if curr in visiting:  # Cycle
            return False
        if prev_map[curr] == []:
            return True

        visiting.add(curr)
        for prev in prev_map[curr]:
            if not dfs(prev):
                return False

        visiting.remove(curr)
        prev_map[curr] = []
        return True

    return all(dfs(i) for i in range(courses))
