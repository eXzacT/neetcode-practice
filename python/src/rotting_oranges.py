from collections import deque

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an m x n grid where each cell can have one of three values:

        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.

    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.'''


@time_execution()
def sol_iter_bfs(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    seen = [[False]*WIDTH for _ in range(HEIGHT)]

    mins = fresh = 0
    queue = deque()

    # Add all the positions of rotten oranges and count how many oranges in total, also how many rotten
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == 2:
                queue.append((i, j))
                seen[i][j] = True
            elif grid[i][j] == 1:
                fresh += 1

    # Can't spoil any oranges since they're all spoiled
    if not fresh:
        return 0
    # Can't spoil any oranges since there are no starting spoiled oranges
    if not queue:
        return -1

    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # In bounds, fresh and didn't see before
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and grid[ni][nj] == 1 and not seen[ni][nj]:
                    seen[ni][nj] = True
                    fresh -= 1
                    queue.append((ni, nj))

            # Wasn't able to spoil any more oranges, are all of them rotten?
            if not queue:
                return mins if fresh == 0 else -1

        mins += 1


@time_execution(executions=1)
def sol_iter_bfs_space_optimized(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    mins = fresh = 0
    queue = deque()

    # Add all the positions of rotten oranges and count how many oranges in total, also how many rotten
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    # Can't spoil any oranges since they're all spoiled
    if not fresh:
        return 0
    # Can't spoil any oranges since there are no starting spoiled oranges
    if not queue:
        return -1

    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # In bounds, fresh and didn't see before
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and grid[ni][nj] == 1:
                    fresh -= 1
                    grid[ni][nj] = 2
                    queue.append((ni, nj))

            # Wasn't able to spoil any more oranges, are all of them rotten?
            if not queue:
                return mins if fresh == 0 else -1

        mins += 1
