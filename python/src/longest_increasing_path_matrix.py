from collections import deque
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution
''' Given a matrix with 'm'*'n' integers, return the length of the longest increasing path in matrix.
    From each cell, you can either move in four directions: left, right, up, or down. 
    You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).'''


@time_execution()
def sol_dp(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)

    pq = [(matrix[i][j], i, j) for i in range(HEIGHT) for j in range(WIDTH)]
    # By first finding to how many adjacent cells we can go from larger numbers, we ensure that DP is populated properly
    pq.sort(reverse=True)
    dp = [[0]*WIDTH for _ in range(HEIGHT)]

    for _, x, y in pq:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                # To get to current position we pick the best value from up/down/left/right, only if the value at newpos is bigger
                dp[x][y] = max(dp[x][y], dp[nx][ny])
        dp[x][y] += 1  # Then just add 1 to count current number

    # Sadly the number can be anywhere in the 2d array
    return max(max(row) for row in dp)


@time_execution()
def sol_rec(matrix: list[list[int]]) -> int:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)

    def helper(x: int, y: int) -> int:
        count = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            # In bounds and in increasing order
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                count = max(count, 1+helper(nx, ny))

        return count

    # Start from each position
    return max(helper(i, j) for i in range(HEIGHT) for j in range(WIDTH))


@time_execution()
def sol_memo(matrix: list[list[int]]) -> int:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    memo = {}

    def helper(x: int, y: int) -> int:
        key = (x, y)
        if key in memo:
            return memo[key]

        count = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            # In bounds and in increasing order
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                count = max(count, 1+helper(nx, ny))

        memo[key] = count
        return count

    # Start from each position
    return max(helper(i, j) for i in range(HEIGHT) for j in range(WIDTH))


@time_execution()
def sol_memo_v2(matrix: list[list[int]]) -> int:
    '''Same as the above version except not using a dictionary since we know exactly what all the keys will be'''
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    dp = [[None]*WIDTH for _ in range(HEIGHT)]

    def helper(x: int, y: int) -> int:
        if dp[x][y]:
            return dp[x][y]

        count = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            # In bounds and in increasing order
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                count = max(count, 1+helper(nx, ny))

        dp[x][y] = count
        return count

    # Start from each position
    return max(helper(i, j) for i in range(HEIGHT) for j in range(WIDTH))


@time_execution()
def sol_stack(matrix: list[list[int]]) -> int:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    res = 0

    stack = [(i, j, 1) for i in range(HEIGHT) for j in range(WIDTH)]
    while stack:
        x, y, dist = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            # In bounds and in increasing order
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                stack.append((nx, ny, dist+1))
            else:
                res = max(res, dist)

    return res


@time_execution()
def sol_topo_dfs(matrix: list[list[int]]) -> int:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    indegree = [[0] * WIDTH for _ in range(HEIGHT)]

    for x in range(HEIGHT):
        for y in range(WIDTH):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] < matrix[x][y]:
                    indegree[x][y] += 1

    # All the verts with an indegree of 0, default dist is 1
    stack = [(x, y, 1) for x in range(HEIGHT)
             for y in range(WIDTH) if indegree[x][y] == 0]

    max_inc_path = 0
    while stack:
        x, y, dist = stack.pop()
        max_inc_path = max(dist, max_inc_path)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                indegree[nx][ny] -= 1
                if indegree[nx][ny] == 0:
                    stack.append((nx, ny, dist+1))

    return max_inc_path


@time_execution()
def sol_topo_bfs(matrix: list[list[int]]) -> int:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    indegree = [[0] * WIDTH for _ in range(HEIGHT)]

    for x in range(HEIGHT):
        for y in range(WIDTH):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] < matrix[x][y]:
                    indegree[x][y] += 1

    # All the verts with an indegree of 0, default dist is 1
    queue = deque([(x, y) for x in range(HEIGHT)
                   for y in range(WIDTH) if indegree[x][y] == 0])

    max_inc_path = 0
    while queue:
        # Add nodes from the next level for every starting node(nodes that had indegree of 1, then 2 etc)
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and matrix[nx][ny] > matrix[x][y]:
                    indegree[nx][ny] -= 1
                    if indegree[nx][ny] == 0:
                        queue.append((nx, ny))

        max_inc_path += 1  # Increment level

    return max_inc_path
