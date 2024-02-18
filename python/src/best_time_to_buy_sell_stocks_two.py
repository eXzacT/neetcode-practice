if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. You may complete as many transactions as you like 
    (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).'''


@time_execution()
def sol_dp(prices: list[int]) -> int:
    # On day 1 we could have either skipped buying or bought the first stock
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0] = [0, -prices[0]]

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i]
                       if i >= 2 else -prices[i])

    return dp[-1][0]


@time_execution()
def sol_dp_v2(prices: list[int]) -> int:
    if len(prices) == 1:
        return 0

    # On day 1, we could have skipped or invested money
    prevprev = [0, -prices[0]]
    # On day 2, we pick the best between not buying on either day or buying on first and selling today
    # Also remember which day was cheaper(max because the values are negated)
    prev = [max(0, prevprev[1]+prices[1]), max(prevprev[1], -prices[1])]

    for i in range(2, len(prices)):  # Start from day 3
        prevprev, prev = prev, [
            max(prev[0], prev[1]+prices[i]), max(prev[1], prevprev[0]-prices[i])]

    return prev[0]


@time_execution()
def sol_rec(prices: list[int]) -> int:
    def helper(idx: int, buying: bool) -> int:
        if idx >= len(prices):
            return 0

        max_profit = 0
        for i in range(idx, len(prices)):
            if buying:  # Skip or buy this one?
                max_profit = max(helper(i+1, True), -
                                 prices[i]+helper(i+1, False), max_profit)
            else:  # Skip or sell now?
                max_profit = max(helper(i+1, False),
                                 prices[i]+helper(i+2, True), max_profit)

        return max_profit

    return helper(0, True)


@time_execution()
def sol_memo(prices: list[int]) -> int:
    memo = {}

    def helper(idx: int, buying: bool) -> int:
        if idx >= len(prices):
            return 0
        key = (idx, buying)
        if key in memo:
            return memo[key]

        max_profit = 0
        for i in range(idx, len(prices)):
            if buying:  # Skip or buy this one?
                max_profit = max(helper(i+1, True), -
                                 prices[i]+helper(i+1, False), max_profit)
            else:  # Skip or sell now?
                max_profit = max(helper(i+1, False),
                                 prices[i]+helper(i+2, True), max_profit)

        memo[key] = max_profit
        return max_profit

    return helper(0, True)


@time_execution()
def sol_rec_v2(prices: list[int]) -> int:
    def helper(i: int, buying: bool) -> int:
        if i >= len(prices):
            return 0

        if buying:  # Skip or buy this one?
            return max(helper(i+1, True), -prices[i]+helper(i+1, False))
        # Skip or sell now?
        return max(helper(i+1, False), prices[i]+helper(i+2, True))

    return helper(0, True)


@time_execution()
def sol_memo_v2(prices: list[int]) -> int:
    memo = {}

    def helper(i: int, buying: bool) -> int:
        if i >= len(prices):
            return 0
        key = (i, buying)
        if key in memo:
            return memo[key]

        if buying:  # Skip or buy this one?
            memo[key] = max(helper(i+1, True), -prices[i]+helper(i+1, False))
            return memo[key]

        # Skip or sell now?
        memo[key] = max(helper(i+1, False), prices[i]+helper(i+2, True))
        return memo[key]

    return helper(0, True)
