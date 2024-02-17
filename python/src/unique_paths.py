import networkx as nx

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' There is a robot on an m x n grid. The robot is initially located at the top-left corner grid[0][0]. 
    The robot tries to move to the bottom-right corner grid[m - 1][n - 1]). 
    The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the goal'''


@time_execution()
def sol_dp(m: int, n: int) -> int:
    dp = [[0]*n for _ in range(m)]
    # 1 unique way to reach any place in first row and any place in first column since we can only go down or right at any point
    for j in range(n):
        dp[0][j] = 1
    for i in range(m):
        dp[i][0] = 1

    # We can reach any other position with sum ways of reach its above and left positions
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]


@time_execution()
def sol_dp_v2(m: int, n: int) -> int:
    prev_row = [1]*n  # 1 unique way to reach any position in the first row

    # We can reach any other position with sum ways of reach its above and left positions
    for _ in range(m-1):
        temp = prev_row
        for j in range(1, n):
            temp[j] = temp[j-1]+prev_row[j]

        prev_row = temp

    return prev_row[-1]


@time_execution()
def sol_rec(m: int, n: int) -> int:
    def helper(i: int, j: int) -> int:
        if i == m-1 and j == n-1:  # Reached the end
            return 1

        if i == m-1:  # Can only go right
            return helper(i, j+1)
        if j == n-1:  # Can only go down
            return helper(i+1, j)
        return helper(i+1, j)+helper(i, j+1)  # Can go both down or right

    return helper(0, 0)


@time_execution()
def sol_memo(m: int, n: int) -> int:
    memo = {(m-1, n-1): 1}

    def helper(i: int, j: int) -> int:
        key = (i, j)
        if key in memo:
            return memo[key]

        if i == m-1:  # Can only go right
            return helper(i, j+1)
        if j == n-1:  # Can only go down
            return helper(i+1, j)

        memo[key] = helper(i+1, j)+helper(i, j+1)  # Can go both down or right
        return memo[key]

    return helper(0, 0)


@time_execution()
def sol_rec_v2(m: int, n: int) -> int:
    def helper(i: int, j: int) -> int:
        if i == m-1 and j == n-1:  # Reached the end
            return 1
        if i == m or j == n:
            return 0

        return helper(i+1, j)+helper(i, j+1)

    return helper(0, 0)


@time_execution()
def sol_memo_v2(m: int, n: int) -> int:
    memo = {(m-1, n-1): 1}

    def helper(i: int, j: int) -> int:
        key = (i, j)
        if key in memo:
            return memo[key]
        if i == m or j == n:
            return 0

        memo[key] = helper(i+1, j)+helper(i, j+1)
        return memo[key]

    return helper(0, 0)


@time_execution()
def sol_nx(m: int, n: int) -> int:
    G = nx.DiGraph()

    def helper(i: int, j: int) -> None:
        if i == m or j == n:
            return

        G.add_edge((i, j), (i+1, j))
        helper(i+1, j)
        G.add_edge((i, j), (i, j+1))
        helper(i, j+1)

    helper(0, 0)
    return len(list(nx.all_simple_paths(G, source=(0, 0), target=(m-1, n-1))))
