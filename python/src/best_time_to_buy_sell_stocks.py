if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''


@time_execution()
def sol_n_squared(prices: list[int]) -> int:
    res = max([prices[j]-prices[i] for i in range(len(prices))
              for j in range(i+1, len(prices))])
    return res if res > 0 else 0


@time_execution()
def sol_n(prices: list[int]) -> int:
    highest_sell = {}
    high = prices[-1]

    for idx in range(len(prices)-1, -1, -1):
        high = max(high, prices[idx])
        highest_sell[idx] = high

    return max([highest_sell[idx]-prices[idx] for idx in range(len(prices))])


@time_execution(executions=1000)
def sol_n_space_time_optimized(prices: list[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i]-min_price)
        min_price = min(min_price, prices[i])

    return max_profit


@time_execution(executions=1000)
def sol_n_space_time_optimized_v2(prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(prices[r]-prices[l], max_profit)
        else:  # We found a cheaper day to buy since right is smaller than left
            l = r
        r += 1

    return max_profit
