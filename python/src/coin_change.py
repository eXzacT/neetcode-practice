import networkx as nx

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer array 'coins' where each element represents the coin value, and an integer 'amount'
    return the fewest number of coins that you need to make up that amount. 
    You can use the same coin value multiple times
    If that amount of money cannot be made up by any combination of the coins, return -1.'''


@time_execution()
def sol_dp(coins: list[int], amount: int) -> int:
    dp = [float('inf')]*(amount+1)
    dp[0] = 0  # To reach sum of 0, we just don't use any coins
    for curr_sum in range(amount+1):
        if dp[curr_sum] != -1:  # If we can reach this amount of money using the coins we have
            for coin in coins:
                if (new_sum := curr_sum+coin) <= amount:
                    dp[new_sum] = min(1+dp[curr_sum], dp[new_sum])

    return dp[-1] if dp[-1] != float('inf') else -1


@time_execution()
def sol_dp_v2(coins: list[int], amount: int) -> int:
    dp = [False]*(amount+1)
    dp[0] = 0  # To reach sum of 0, we just don't use any coins
    for curr_sum in range(amount+1):
        if dp[curr_sum] or curr_sum == 0:  # If we can reach this amount of money using the coins we have
            for coin in coins:
                if (new_sum := curr_sum+coin) <= amount:
                    if dp[new_sum]:  # We already found a way to get to this sum, is this one better?
                        dp[new_sum] = min(1+dp[curr_sum], dp[new_sum])
                    else:  # First time here
                        dp[new_sum] = 1+dp[curr_sum]

    return -1 if type(dp[-1]) == bool else dp[-1]


@time_execution()
def sol(coins: list[int], amount: int) -> int:
    def helper(remainder: int) -> int:
        if remainder == 0:
            return 0

        res = float('inf')
        for coin in coins:
            if (x := remainder-coin) >= 0:
                res = min(res, 1+helper(x))

        return res

    res = helper(amount)
    return res if res != float('inf') else -1


@time_execution()
def sol_memo(coins: list[int], amount: int) -> int:
    memo = {0: 0}

    def helper(remainder: int) -> int:
        if remainder in memo:
            return memo[remainder]

        res = float('inf')
        for coin in coins:
            if (x := remainder-coin) >= 0:
                res = min(res, 1+helper(x))

        memo[remainder] = res
        return res

    res = helper(amount)
    return res if res != float('inf') else -1


@time_execution()
def sol_v2(coins: list[int], amount: int) -> int:
    def helper(remainder: int) -> int:
        if remainder == 0:
            return 0

        return min([1+helper(remainder-coin) for coin in coins if remainder-coin >= 0] or [float('inf')])

    res = helper(amount)
    return res if res != float('inf') else -1


@time_execution()
def sol_v2_memo(coins: list[int], amount: int) -> int:
    memo = {0: 0}

    def helper(remainder: int) -> int:
        if remainder in memo:
            return memo[remainder]

        memo[remainder] = min([1+helper(remainder-coin)
                              for coin in coins if remainder-coin >= 0] or [float('inf')])
        return memo[remainder]

    res = helper(amount)
    return res if res != float('inf') else -1


@time_execution()
def sol_nx(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    G = nx.DiGraph()

    def create_graph(remainder: int) -> None:
        if remainder == 0:
            return

        for coin in coins:
            if (new := remainder-coin) >= 0:
                G.add_edge(remainder, new)
                create_graph(new)

    create_graph(amount)
    return nx.shortest_path_length(G, source=amount, target=0) if G.has_node(0) else -1
