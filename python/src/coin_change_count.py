import matplotlib.pyplot as plt
import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer array 'coins' where each element represents the coin value, and an integer 'amount'
    return the number of combinations you can use to make up that amount. 
    You can use the same coin value multiple times.
    If that amount of money cannot be made up by any combination of the coins, return 0.'''


@time_execution()
def sol_dp(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make zero (with no coins)
    for coin in coins:
        # To get from 7 to 10, we can for example add 3(if we have that coin)
        # So for all ways that we can construct 7, we can also add 3 and get to 10
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[-1]


@time_execution()
def sol_rec(amount: int, coins: list[int]) -> int:
    def helper(idx: int, remainder: int) -> int:
        if remainder == 0:
            return 1

        count = 0
        # Only consider coins after the last used one to avoid permutations
        for i in range(idx, len(coins)):
            if (x := remainder-coins[i]) >= 0:
                count += helper(i, x)

        return count

    return helper(0, amount)


@time_execution()
def sol_memo(amount: int, coins: list[int]) -> int:
    memo = {}

    def helper(idx: int, remainder: int) -> int:
        if remainder == 0:
            return 1
        key = (idx, remainder)
        if key in memo:
            return memo[key]

        count = 0
        # Only consider coins after the last used one to avoid permutations
        for i in range(idx, len(coins)):
            if (x := remainder-coins[i]) >= 0:
                count += helper(i, x)

        memo[key] = count
        return count

    return helper(0, amount)


@time_execution()
def sol_rec_v2(amount: int, coins: list[int]) -> int:
    def helper(idx: int, remainder: int) -> int:
        if idx == len(coins) or remainder < 0:
            return 0
        if remainder == 0:
            return 1

        return helper(idx, remainder-coins[idx]) + helper(idx+1, remainder)

    return helper(0, amount)


@time_execution()
def sol_memo_v2(amount: int, coins: list[int]) -> int:
    memo = {}

    def helper(idx: int, remainder: int) -> int:
        if idx == len(coins) or remainder < 0:
            return 0
        if remainder == 0:
            return 1
        key = (idx, remainder)
        if key in memo:
            return memo[key]

        memo[key] = helper(idx, remainder-coins[idx]) + \
            helper(idx+1, remainder)
        return memo[key]

    return helper(0, amount)


@time_execution()
def sol_nx(amount: int, coins: list[int]) -> int:
    G = nx.DiGraph()
    if amount == 0:
        return 1

    G.add_node((0, amount))
    queue = [(0, amount)]

    while queue:
        idx, remainder = queue.pop(0)
        if remainder == 0:
            continue
        if idx < len(coins):
            # Take the coin if the remainder doesn't go under 0
            if (x := remainder - coins[idx]) >= 0:
                next_state = (idx, x)
                queue.append(next_state)
                G.add_edge((idx, remainder), next_state)

            # Don't take the coin
            next_state = (idx + 1, remainder)
            queue.append(next_state)
            G.add_edge((idx, remainder), next_state)

    # Find all paths that lead to a remainder of 0, which implies a successful combination
    paths = 0
    for idx in range(len(coins) + 1):
        if G.has_node((idx, 0)):
            paths += len(list(nx.all_simple_paths(G,
                         source=(0, amount), target=(idx, 0))))

    return paths
