from collections import deque
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.'''


@time_execution()
def sol_dfs(grid: list[list[str]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    seen = [[False]*WIDTH for _ in range(HEIGHT)]

    def mark_adjacent(i: int, j: int) -> None:
        seen[i][j] = True
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and not seen[ni][nj] and grid[ni][nj] == '1':
                mark_adjacent(ni, nj)

    islands = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == '1' and not seen[i][j]:
                islands += 1
                mark_adjacent(i, j)

    return islands


@time_execution()
def sol_dfs_iter(grid: list[list[str]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    seen = [[False]*WIDTH for _ in range(HEIGHT)]

    def mark_adjacent(i: int, j: int) -> None:
        queue = [(i, j)]
        seen[i][j] = True
        while queue:
            i, j = queue.pop()

            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and grid[ni][nj] == '1' and not seen[ni][nj]:
                    seen[ni][nj] = True
                    queue.append((ni, nj))

    islands = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == '1' and not seen[i][j]:
                islands += 1
                mark_adjacent(i, j)

    return islands


@time_execution()
def sol_bfs(grid: list[list[str]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    seen = [[False]*WIDTH for _ in range(HEIGHT)]

    def mark_adjacent(i: int, j: int) -> None:
        queue = deque([(i, j)])
        seen[i][j] = True
        while queue:
            i, j = queue.popleft()

            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and grid[ni][nj] == '1' and not seen[ni][nj]:
                    queue.append((ni, nj))
                    seen[ni][nj] = True

    islands = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == '1' and not seen[i][j]:
                islands += 1
                mark_adjacent(i, j)

    return islands
