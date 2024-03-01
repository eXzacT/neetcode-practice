if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
    (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.'''


@time_execution()
def sol_dfs(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    seen = [[False]*WIDTH for _ in range(HEIGHT)]

    def dfs(i: int, j: int) -> int:
        if i < 0 or i >= HEIGHT or j < 0 or j >= WIDTH or not grid[i][j] or seen[i][j]:
            return 0

        seen[i][j] = True
        return 1+dfs(i-1, j)+dfs(i+1, j)+dfs(i, j-1)+dfs(i, j+1)

    res = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] and not seen[i][j]:
                res = max(res, dfs(i, j))

    return res


@time_execution()
def sol_dfs_iter(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    seen = [[False]*WIDTH for _ in range(HEIGHT)]

    def dfs(i: int, j: int) -> int:
        stack = [(i, j)]
        count = 0
        while stack:
            i, j = stack.pop()
            count += 1
            seen[i][j] = True

            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and grid[ni][nj] and not seen[ni][nj]:
                    seen[ni][nj] = True
                    stack.append((ni, nj))

        return count

    res = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] and not seen[i][j]:
                res = max(res, dfs(i, j))

    return res
