import networkx as nx

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


''' You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''


@time_execution()
def sol_dp_v1(n: int) -> int:
    if n == 1:
        return 1

    dp = [0]*(n)
    dp[0] = 1  # 1 way to climb 1 stair
    dp[1] = 2  # 2 ways to climb 2 stairs, 1+1 or 2
    for i in range(2, n):  # For all the others, ways to climb them is equal to the sum of the 2 steps before it
        dp[i] += dp[i-1]+dp[i-2]

    return dp[-1]


@time_execution()
def sol_dp_v2(n: int) -> int:
    if n <= 3:
        return n

    prevprev = 2
    prev = 3
    for _ in range(3, n):
        prevprev, prev = prev, prev+prevprev

    return prev


@time_execution()
def sol_rec(n: int) -> int:
    def helper(remaining: int) -> int:
        if remaining == 0:
            return 1

        ways = 0
        for step in [1, 2]:
            if (x := remaining-step) >= 0:
                ways += helper(x)

        return ways

    return helper(n)


@time_execution()
def sol_memo(n: int) -> int:
    memo = {0: 1}

    def helper(remaining: int) -> int:
        if remaining in memo:
            return memo[remaining]

        ways = 0
        for step in [1, 2]:
            if (x := remaining-step) >= 0:
                ways += helper(x)

        memo[remaining] = ways
        return ways

    return helper(n)


@time_execution()
def sol_rec_v2(n: int) -> int:
    def helper(remaining: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0

        return helper(remaining-1)+helper(remaining-2)

    return helper(n)


@time_execution()
def sol_memo_v2(n: int) -> int:
    memo = {0: 1}

    def helper(remaining: int) -> int:
        if remaining in memo:
            return memo[remaining]
        if remaining < 0:
            return 0

        memo[remaining] = helper(remaining-1)+helper(remaining-2)
        return memo[remaining]

    return helper(n)


@time_execution()
def sol_tail_rec(n: int) -> int:
    def helper(n: int, prev: int = 1, curr: int = 2) -> int:
        if n == 1:
            return prev

        return helper(n-1, curr, prev+curr)

    return helper(n)


@time_execution()
def sol_nx(n: int) -> int:
    G = nx.DiGraph()

    def helper(remainder: int) -> None:
        if remainder <= 0:
            return

        G.add_edge(remainder, remainder-1)
        G.add_edge(remainder, remainder-2)
        helper(remainder-1)
        helper(remainder-2)

    helper(n)
    return len(list(nx.all_simple_paths(G, source=n, target=0)))
