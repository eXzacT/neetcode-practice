if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
    The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
    
    You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level at that coordinate.
    The island receives a lot of rain water, and that rain water can flow into the ocean if there is a decreasing path from current position to the ocean.
    Water is allowed to travel north, south, east and west, not diagonally.
    
    Return a list of all the positions(tuples(x,y)) where the rain water can travel to both oceans.'''


@time_execution()
def sol_dfs(heights: list[list[int]]) -> list[tuple[int, int]]:
    if not heights or not heights[0]:
        return []

    WIDTH, HEIGHT = len(heights[0]), len(heights)
    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs(i: int, j: int, reachable: set):
        if (i, j) in reachable:
            return
        reachable.add((i, j))
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and heights[ni][nj] >= heights[i][j]:
                dfs(ni, nj, reachable)

    for i in range(HEIGHT):
        dfs(i, 0, pacific_reachable)
        dfs(i, WIDTH-1, atlantic_reachable)
    for j in range(WIDTH):
        dfs(0, j, pacific_reachable)
        dfs(HEIGHT-1, j, atlantic_reachable)

    return sorted(list(pacific_reachable & atlantic_reachable))


@time_execution()
def sol_dfs_iterative(heights: list[list[int]]) -> list[tuple[int, int]]:
    if not heights or not heights[0]:
        return []

    WIDTH, HEIGHT = len(heights[0]), len(heights)
    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs_iterative(reachable: set, stack: list[tuple[int, int]]) -> None:
        while stack:
            i, j = stack.pop()
            if (i, j) in reachable:
                continue
            reachable.add((i, j))
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and heights[ni][nj] >= heights[i][j] and (ni, nj) not in reachable:
                    stack.append((ni, nj))

    # Initialize the stack with border cells for both oceans
    pacific_stack = [(i, 0) for i in range(HEIGHT)] + \
        [(0, j) for j in range(WIDTH)]
    atlantic_stack = [(i, WIDTH - 1) for i in range(HEIGHT)] + \
        [(HEIGHT - 1, j) for j in range(WIDTH)]

    # Perform iterative DFS from both oceans
    dfs_iterative(pacific_reachable, pacific_stack)
    dfs_iterative(atlantic_reachable, atlantic_stack)

    # Intersection of cells reachable from both oceans
    return sorted(list(pacific_reachable & atlantic_reachable))
