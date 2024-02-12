import networkx as nx

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


''' You are given an integer array costs where cost[i] is the cost of ith step on a staircase. 
    You can either start from the step with index 0, or the step with index 1.
    And depending on which stair you end up on, you have to pay that cost.
    Return the minimum cost to reach the top of the floor.'''


@time_execution()
def sol_dp(costs: list[int]) -> int:
    dp = [0]*(len(costs))
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, len(costs)):
        dp[i] += costs[i]+min(dp[i-1], dp[i-2])

    return min(dp[-1], dp[-2])


@time_execution()
def sol_dp_v2(costs: list[int]) -> int:
    prev = costs[0]
    curr = costs[1]

    for i in range(2, len(costs)):
        prev, curr = curr, min(prev, curr)+costs[i]

    return min(prev, curr)


@time_execution()
def sol_rec(costs: list[int]) -> int:
    def helper(i: int) -> int:
        if i == len(costs):
            return 0
        if i == len(costs)-1:
            return costs[i]

        return costs[i]+min(helper(i+1), helper(i+2))

    return min(helper(0), helper(1))


@time_execution()
def sol_memo(costs: list[int]) -> int:
    memo = {len(costs): 0}

    def helper(i: int) -> int:
        if i in memo:
            return memo[i]
        if i == len(costs)-1:
            return costs[i]

        memo[i] = costs[i]+min(helper(i+1), helper(i+2))
        return memo[i]

    return min(helper(0), helper(1))


@time_execution()
def sol_nx(costs: list[int]) -> int:
    G = nx.DiGraph()
    n = len(costs)
    dummy = -1

    # Add edges for each step
    for i in range(n):
        if i+1 == n or i+2 == n:
            G.add_edge(i, dummy, weight=0)
        if i + 1 < n:
            G.add_edge(i, i + 1, weight=costs[i + 1])
        if i + 2 < n:
            G.add_edge(i, i + 2, weight=costs[i + 2])

    # Min price starting from 0th position and 1st position
    return min(costs[i]+nx.shortest_path_length(G, source=i, target=dummy, weight="weight") for i in range(2))
