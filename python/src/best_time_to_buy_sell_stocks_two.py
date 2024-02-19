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
    n = len(prices)

    if n == 1:
        return 0

    buy = [0]*n
    sell = [0]*n

    # Which day was better to buy, day 1 or day 2, also was it worth selling on day 2?
    buy[1] = max(-prices[0], -prices[1])
    sell[1] = max(0, -prices[0]+prices[1])

    # For all the other days we do this(technically the formula is same for day 2 except for buying), because on day 1 we couldn't have possibly come from day -1(2 days before)
    # To reach sell[i] we could have come here from same profit we had yesterday OR sell what we bought previously
    # To reach buy[i] we could have come here from holding what we have bought previously OR from selling 2 days ago
    for i in range(2, len(prices)):  # Start from day 3
        sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        buy[i] = max(buy[i-1], sell[i-2]-prices[i])

    return sell[-1]


@time_execution()
def sol_dp_v2(prices: list[int]) -> int:
    '''Same as above but with O(1) memory'''
    if len(prices) == 1:
        return 0

    prevprev_sell = 0  # Day 1
    # Which day was better to buy, day 1 or day 2, also was it worth selling on day 2?
    prev_buy, prev_sell = max(-prices[0], -prices[1]), max(0, -prices[0]+prices[1])\

    for i in range(2, len(prices)):  # Start from day 3
        prevprev_sell, prev_sell, prev_buy = prev_sell, max(
            prev_sell, prev_buy+prices[i]), max(prev_buy, prevprev_sell-prices[i])

    return prev_sell


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
